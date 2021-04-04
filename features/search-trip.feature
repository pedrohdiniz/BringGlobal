Feature: Search a Trip

  @search-trip
  Scenario: Success search for a trip between Lisbon and Paris
    Given I am at RyanAir main page
    When I search for a trip between Lisbon and Paris
    And I Select best price
    And I select a seat
    And I select a bag
    Then I finish my trip plan


