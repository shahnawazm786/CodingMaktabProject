import pytest
@pytest.mark.dashboard
def test_originator_dashboard():
    print('Originator Dashboard')

@pytest.mark.dashboard
def test_participant_dashboard():
    print('Participant Dashboard')

@pytest.mark.dashboard
def test_reviewer_dashboard():
    print('Reviewer Dashboard')

@pytest.mark.dashboard
def test_proxy_reviewer_dashboard():
    print('Proxy reviewer Dashboard')

@pytest.mark.dashboard
def test_approval_dashboard():
    print('Appproval Dashboard')

@pytest.mark.others
def test_others():
    print('Test Others')
    assert True