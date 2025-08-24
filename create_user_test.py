import sender_stand_request

def test_order_creation():
    creation_response = sender_stand_request.post_new_order()
    track_id = creation_response.json()['track']
    response = sender_stand_request.get_orders_track(track_id)
    assert response.status_code == 200