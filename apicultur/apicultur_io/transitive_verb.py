#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apicultur.service import Service

class TransitiveVerb(Service):
    # # http://apicultur.io/apis/info?name=VerbTransitive_Onoma_es&version=1.0.0&provider=molinodeideas
    version = '1.0.0'
    endpoint = 'onoma/conjugator/es/transitiveverb'
    method = 'GET'
    arguments = ['infinitivo',]
    func_name = 'transitive_verb'

    def get_endpoint(self):
        return self._join_url(self.endpoint, self.version, '?infinitivo=%(infinitivo)s')
