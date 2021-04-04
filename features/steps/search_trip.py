from behave import given, when, then
from features.pages.search_trip import SearchTrip
from features.pages.select_flight import SelectFlight
from features.pages.select_bag import SelectBag
from features.pages.select_seat import SelectSeat

@given('I am at RyanAir main page')
def step_implementation(context):
    context.driver.get(context.url)

@when('I search for a trip between Lisbon and Paris')
def step_implementation(context):
    context.search_trip = SearchTrip(context.driver)
    context.search_trip.search_flights()

@when('I Select best price')
def step_implementation(context):
    context.select_flight = SelectFlight(context.driver)
    context.select_flight.select_price()

@when('I select a seat')
def step_implementation(context):
    context.select_seat = SelectSeat(context.driver)
    context.select_seat.select_seat()

@when('I select a bag')
def step_implementation(context):
    context.select_bag = SelectBag(context.driver)
    context.select_bag.select_bag()

@then('I finish my trip plan')
def step_implementation(context):
    context.select_bag = SelectBag(context.driver)
    message = context.select_bag.finish_plan()
    assert message == 'Plan your whole trip'

