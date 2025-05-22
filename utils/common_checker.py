import allure
from deepdiff import DeepDiff


@allure.step('Check The Difference Between Objects')

def check_difference_between_objects(actual_result, expected_result) -> None:
    comparison_data=(actual_result, expected_result)
    diff = DeepDiff(
        *comparison_data,
        ignore_order=True
    )
    assert not diff, f"Difference: {diff}"