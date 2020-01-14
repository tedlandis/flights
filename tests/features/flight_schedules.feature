Feature: Check Flight Schedules

As a traveler 
I need to check flight schedules
So that I do not miss my plane.


Scenario: Check Montreal to Paris flights
    Given I am on "/"
    When I wait for 3 seconds
    And I enter "YUL" in the "fsc-origin-search" field
    And I enter "CDG" in the "fsc-destination-search" field
    And I press "Search flights"
    And I wait for 12 seconds
    Then I can see "Montreal (YUL) - Paris (CDG)" on the page
    And the checkbox "direct" is checked


Scenario: Check Madrid to Dubai flights
    Given I am on "/"
    When I wait for 3 seconds
    And I enter "MAD" in the "fsc-origin-search" field
    And I enter "Dubai" in the "fsc-destination-search" field
    And I press "Search flights"
    And I wait for 12 seconds
    Then I can see "Madrid (MAD) - Dubai (Any)" on the page
    And the checkbox "oneStop" is checked


Scenario: Check Milan to Toronto flights
    Given I am on "/"
    When I wait for 3 seconds
    And I enter "Milan" in the "fsc-origin-search" field
    And I enter "YYZ" in the "fsc-destination-search" field
    And I press "Search flights"
    And I wait for 12 seconds
    Then I can see "Milan (Any) - Toronto (YYZ)" on the page
    And the checkbox "direct" is not checked
