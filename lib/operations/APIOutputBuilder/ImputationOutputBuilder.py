from lib.operations.APIOutputBuilder.APIOutputBuilder import APIOutputBuilder
from lib.operations.OperationOutput import OperationOutput


class SingleColImputationOutputBuilder(APIOutputBuilder):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__()

    def get_operation_results(self, operationOutput: OperationOutput) -> dict:
        imputation_stat = operationOutput.processStats[0]
        is_imputed = imputation_stat["imputed_count"] > 0
        col_name = imputation_stat["col_name"]
        imputation_result = (
            imputation_stat
            if is_imputed
            else "No need of data imputation for column " + col_name + " !"
        )

        results = {"data": {"imputed": is_imputed, "result": imputation_result}}

        return results


class AutoImputationOutputBuilder(APIOutputBuilder):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__()

    def get_operation_results(self, operationOutput: OperationOutput) -> dict:
        imputation_stat = operationOutput.processStats.get(
            "affected_col_stats", "No need of data imputation!!"
        )
        imputer_type = operationOutput.processStats.get("imputer_type", "Null")
        results = {"Imputer selected": imputer_type, "data": imputation_stat}

        return results
