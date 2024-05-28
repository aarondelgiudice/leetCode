import time

from typing import List, Callable


def test(test_cases: List, fn: Callable):
    success = 0
    start_time = time.time()

    for inputs, expected in test_cases:
        current_start_time = time.time()

        actual = fn(*inputs)

        current_end_time = time.time()
        current_total_time = round(current_end_time - current_start_time, 4)

        assert actual == expected, f"Expected {expected}, but got {actual}."

        if actual == expected:
            print(
                f"✅ solution({inputs}) returned {actual}. Took {current_total_time}s."
            )

            success += 1

        else:
            print(f"❌ solution({inputs}) returned {actual}, but expected {expected}.")

    end_time = time.time()
    total_time = round(end_time - start_time, 4)

    assert success == len(test_cases), f"❌ {len(test_cases)-success} test(s) failed."

    print(f"\n✅ {success} test(s) passed! Took {total_time}s.")

    return
