import os
import polars as pl
from ml_project.entity.config_entity import DataValidationConfig
from ml_project.utils.common import create_dirs

import logging

class ValidateSchemaError(BaseException):
    pass


class DataValidation:
    def __init__(self, config: DataValidationConfig) -> None:
        self.config = config
        self.logger = logging.getLogger("ml_project.component.DataValidation")

        create_dirs([self.config.stage_dir])

    def _validate_data(self) -> bool:
        validation_status = True
        ref_schema = self.config.data_schema
        ref_cols = ref_schema.keys()

        df = pl.read_csv(os.path.join(self.config.data_dir, "card_transdata.csv"))
        df_schema = df.schema

        with open(self.config.validation_result_file, "w") as f:
            for col, dtype in df_schema.items():
                if col not in ref_cols:
                    validation_status = False
                    f.write(f"> Found an unexpected column ({col}) in data\n")
                else:
                    try:
                        if not (dtype == pl.__getattribute__(ref_schema[col])):
                            validation_status = False
                            f.write(f"> Data type of {col} doesn't match the schema\n")
                    except AttributeError:
                        validation_status = False
                        f.write(f"> Found an unexpected data type {dtype} of {col}\n")
            if not validation_status:
                f.write("-" * 80 + "\n")
            f.write(f"Validation status: {validation_status}")

        return validation_status

    def execute(self) -> None:
        validation_status = self._validate_data()
        if not validation_status:
            self.logger.error("Failed to validate data")
            raise ValidateSchemaError(
                f"Failed to validate data schema. See {self.config.validation_result_file} for more details"
            )
        else:
            self.logger.info("Validated data")
