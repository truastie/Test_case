def validate_response(response, model, status_code):
    print('Ожидали статус:', status_code)
    print('Фактический статус:', response.status_code)
    print('Тело ответа:', response.text)
    assert response.status_code == status_code
    return model.model_validate(response.json())