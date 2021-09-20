import pytest
import datetime as dt
from numbers import Number


def make_early_bird_ticket() -> Ticket:
    """
    Basic ticket for testing
    :return: Ticket
    """
    return Ticket("Wild Carrot 2021", TicketType.EARLYBIRD)


def test_ticket_has_account():
    ticket = make_early_bird_ticket()
    assert isinstance(ticket.account, Account)


def test_ticket_type_is_correctly_set():
    ticket = make_early_bird_ticket()
    assert ticket.type == TicketType.EARLYBIRD


def test_invalid_ticket_type_rejected():
    with pytest.raises(ValueError):
        Ticket("Wild Carrot 2021", "INVALID_TICKET_TYPE")


def test_ticket_linked_to_festival():
    festival_name = "Wild Carrot 2021"
    ticket = Ticket(festival_name, TicketType.EARLYBIRD)
    assert ticket.festival.name == festival_name


def test_successfully_change_ticket_type():
    ticket = make_early_bird_ticket()
    ticket.type = TicketType.STANDARD
    assert ticket.type == TicketType.STANDARD


def test_ticket_status_after_creation():
    ticket = make_early_bird_ticket()
    ticket.status == TicketStatus.ISSUED


def test_ticket_status_after_checkin():
    # incorrect - this does not make sense!
    ticket = make_early_bird_ticket()
    ticket.assign_to_account(account_id=12)
    assert ticket.status == TicketStatus.ASSIGNED


def test_ticket_has_price():
    ticket = make_early_bird_ticket()
    assert isinstance(ticket.price, float)


def test_ticket_has_issue_date():
    ticket = make_early_bird_ticket()
    assert isinstance(ticket.issue_dt, dt.datetime)


def test_ticket_has_topup_amount():
    ticket = make_early_bird_ticket()
    assert isinstance(ticket.topup_amount, Number)


def test_ticket_topup_amout_is_5():
    ticket = make_early_bird_ticket()
    assert ticket.topup_amount == 5
