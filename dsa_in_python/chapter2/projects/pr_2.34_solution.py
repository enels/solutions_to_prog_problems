import string


class BarChart:

    def __init__(self, filepath):
        with open(filepath) as fp:
            self._lines = fp.readlines()

    def _frequency(self):
        """
        Get the frequency of each character in the lines in file
        """


        # container to uniquely store each of the character
        char_set = set()

        list_lines = list()
        char_freq = dict()

        # store each unique character
        for line in self._lines:
            line = line.lower()
            for c in line:
                # remvove the punctuations
                if c in string.punctuation or c == " " or c == "\n":
                    pass
                else:
                    char_set.add(c)
                    list_lines.append(c)

        # initialize the character frequency to zero
        for c in char_set:
            char_freq[c] = 0

        # get the frequencies
        for c in list_lines:
            char_freq[c] += 1

        return char_freq

    def _max_frequency(self):
        frequency = self._frequency()

        max_dict = dict()
        max = 0

        print("frequency {}".format(frequency))

        # iterate through the frequency dict to get the maximum value
        for k,v in frequency.items():
            if v > max:
                max_dict[k] = v
                max = v

        return max_dict

    def plot_graph(self):
        """
        Plot the frequencies of the characters in the file using a bar chart
        """
        # get alphabet with the largest frequency
        max_alphabet = self._max_frequency()

        # get the maximum alphabet in dictionary form
        max_alphabet_dict = max_alphabet.popitem()

        # get the highest bar value
        max_bar_value = max_alphabet_dict[1]

        # get the character frequencies
        char_freqs = self._frequency()

        for val in range(max_bar_value, 0, -1):
            for k,v in char_freqs.items():
                # get the current alphabet value
                current_alpha_value = char_freqs[k]
                if current_alpha_value == val:
                    # print the bar
                    print("|", end=" ")

                    # reduce the current alphabet count by one
                    char_freqs[k] = current_alpha_value - 1
                else:
                    print(" ", end=" ")
            print("")   # end of row

        # print out the characters
        char_freqs = self._frequency()
        for k in char_freqs:
            print(k, end=" ")

        print("")


if __name__ == "__main__":
    file = "textdoc"
    chart = BarChart(file)
    chart.plot_graph()