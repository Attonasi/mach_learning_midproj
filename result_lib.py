"""
Class: Result

Purpose: Takes two lists. They are intended to be a list of predicted values and a list
    of true values. Creating an instance of this class will give you access to values
    derived from the two lists that are potentially useful in assessing your predictions.

    Optional parameter is a Range of acceptable values that will be compared to the
    absolute value of predicted[i] - thruth[i] to determine successful result counts

Signature __init__: Result: List, List -> Result
                    Result: List, List, Float -> Result

Result.<values>:

    List list_variances: list of the differences between the predicted and true values.
        The list is left natural so there are positive and negative numbers for more
        accurate plotting and assessment. They are left in the original indexes as well.

    List sorted.list.variances: list of variances in sorted order and by absolute value.

    Float average_variance: The average difference between predicted and true value

    Float number_correct: compares the absolute value of each predicted value - truth
        to default 1 or a given range and counts the number correct

    Float percent_correct: number_correct / len(list)

    Float average_variance: sum/len

    Float std_dev_variances: Standard deviation of the variances.

    Float total_variance: straight total of adding the actual values to the total. Can
        be positive or negative.

Result.<methods>

    Result.display_total() will print the Range, Count of the predictions that are
        within the range of the true value, and the mean variance between prediction
        and truth.

        Signature: Result.display_totals: (void) -> (void)

    Result.get_confidence_interval(Integer) will take the given number, multiply it
        by the len of the lists given, divide that by 100 and round up. It will use
        that total as the index and return the value from Result.sorted_list_variances.
        This will tell you what variance size you need to accept to get that confidence
        interval.

        Signature: Result.get_confidence_interval_value: 0 < Integer < 100 -> Float

"""
import pandas as pd

class Result:
    # def __init__(self, pred, truth):
    #     if len(pred) != len(truth):
    #         self.error = True
    #         print('Error: The lists provided are not the same length')
    #         return
    #     self.error = False
    #     self.range = 1
    #     self.total_variance = 0
    #     self.list_variances = self.get_variance_list(pred, truth)
    #     self.sorted_list_variances = self.self_quicksort(self.list_variances)
    #     self.correct = self.find_correct()
    #     self.mean_variance = self.get_mean_total_variance()

    def __init__(self, pred, truth, given_range):
        if len(pred) != len(truth):
            self.error = True
            print('Error: The lists provided are not the same length')
            return
        self.error = False
        self.range = given_range
        self.total_variance = 0
        self.list_variances = self.get_variance_list(pred, truth)
        self.sorted_list_variances = self.self_quicksort(self.list_variances)
        self.correct = self.find_correct()
        self.percent_correct = self.correct / len(self.sorted_list_variances)
        self.mean_variance = self.get_mean_total_variance()

    def find_correct(self):
        correct = 0
        for val in self.sorted_list_variances:
            if self.range >= val:
                correct += 1
            else:
                return correct
        return correct

    def get_variance_list(self, pred, truth):
        list = []
        for i in range(len(pred)):
            list.append(pred[i] - truth[i])
        return list

    def get_mean_total_variance(self):
        total = 0
        for val in self.list_variances:
            self.total_variance += val
            total += abs(val)
        return total / len(self.list_variances)

    def display_totals(self):
        if self.error:
            print('The current Result object is blank. Most likely due to incorrect inputs')
        else:
            print('Range: ' + str(self.range))
            print('Correct: ' + str(self.correct))
            print('Mean Variance: ' + str(self.mean_variance))

    def get_confidence_interval(self, inter_range):
        if 0 > inter_range > 100:
            print('Invalid percentage')
            return 0
        if len(self.sorted_list_variances) < 2:
            print('List is too short to get a confidence interval')
        return self.sorted_list_variances[-(-(inter_range * len(self.list_variances)) // 100)]

    def self_quicksort(self, list_to_sort):
        if len(list_to_sort) < 2:
            return list_to_sort
        else:
            less = []
            equal = []
            greater = []
            pivot = abs(list_to_sort[0])
            for val in list_to_sort:
                val = abs(val)
                if val < pivot:
                    less.append(val)
                elif val > pivot:
                    greater.append(val)
                else:
                    equal.append(val)
            return self.self_quicksort(less) + equal + self.self_quicksort(greater)
