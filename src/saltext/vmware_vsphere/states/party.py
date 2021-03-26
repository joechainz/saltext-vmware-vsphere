def cool(name, bang='42'):
    return {'name': name, 'result': True, 'comment': "Does it blend?", 'changes': {'bang':__pillar__.get('bang', bang)}}