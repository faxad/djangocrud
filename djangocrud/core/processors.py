
def global_context(request):
    entity_name = request.get_full_path().split('/')[1]

    return {'entity_title': entity_name}
