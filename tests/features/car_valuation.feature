Feature: Car Valuation
# This feature is to check for the given input car numbers matches the expected data in the given output files

  Scenario: Validate car details
    Given a set of car reg numbers from input file "car_input.txt"
    And the expected details for the car reg from output file "car_output.txt"
    When performs check for each car on the motorway website
    Then verify car details from the website matches to output
