class SubstringFinder:
    longest_substring = ''

    def __init__(self, input_string):
        posssible_substrings = self.get_substrings(input_string)
        self.get_longest_string(posssible_substrings)


    def get_substrings(self, input_string: str):
        substrings = []
        seen = []

        substring = ''
        for letter in input_string:
            if letter in seen:
                substrings.append(substring)

                first_index = self.get_first_char_index(seen, letter)
                substring = substring[first_index + 1:]
                seen = seen[first_index + 1:]
            substring += letter
            seen.append(letter)
        if substring:
            substrings.append(substring)

        return substrings

    
    def get_first_char_index(self, seen_string: list, char: str):
        for i in range(0, len(seen_string)):
            if seen_string[i] == char:
                return i
    

    def get_longest_string(self, possible_substrings: list):
        current_longest = possible_substrings[0];
        for i in range(1,len(possible_substrings)):
            if len(possible_substrings[i]) > len(current_longest):
                current_longest = possible_substrings[i]

        self.longest_substring = current_longest





