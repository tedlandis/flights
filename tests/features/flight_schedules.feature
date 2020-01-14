Feature: Check Flight Schedules

As a traveler I need to check flight schedules
So that I do not miss my plane.

Scenario: Check Montreal to Paris flights
    Given I am on "/"
    When I wait for 3 seconds
    And I enter "YUL" in the "fsc-origin-search" field
    And I enter "CDG" in the "fsc-destination-search" field
    And I press "Search flights"
    And I wait for 12 seconds
    Then the checkbox "direct" is checked
    And I can see "Montreal (YUL) - Paris (CDG)" on the page
