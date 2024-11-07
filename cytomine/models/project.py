# -*- coding: utf-8 -*-

# * Copyright (c) 2009-2024. Authors: see NOTICE file.
# *
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# *      http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
# * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# * See the License for the specific language governing permissions and
# * limitations under the License.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from cytomine import Cytomine


from cytomine.models.collection import Collection
from cytomine.models.model import Model


class Project(Model):
    def __init__(self, name=None, id_ontology=None, **attributes):
        super().__init__()
        self.name = name
        self.ontology = id_ontology
        self.ontologyName = None
        self.blindMode = None
        self.numberOfSlides = None
        self.numberOfImages = None
        self.numberOfAnnotations = None
        self.retrievalProjects = None
        self.numberOfReviewedAnnotations = None
        self.retrievalDisable = None
        self.retrievalAllOntology = None
        self.isClosed = None
        self.isReadOnly = None
        self.hideUsersLayers = None
        self.hideAdminsLayers = None

        self.admins = None
        self.users = None
        self.mode = None
        self.populate(attributes)

    def add_user(self, id_user, admin=False):
        if admin:
            return Cytomine.get_instance().post(
                f"project/{self.id}/user/{id_user}/admin.json"
            )

        return Cytomine.get_instance().post(f"project/{self.id}/user/{id_user}.json")

    def delete_user(self, id_user, admin=False):
        if admin:
            return Cytomine.get_instance().delete(f"project/{self.id}/user/{id_user}/admin.json")

        return Cytomine.get_instance().delete(f"project/{self.id}/user/{id_user}.json")


class ProjectCollection(Collection):
    def __init__(self, filters=None, max=0, offset=0, **parameters):
        super().__init__(Project, filters, max, offset)
        self._allowed_filters = [None, "user", "ontology"]
        self.set_parameters(parameters)

    def save(self, *args, **kwargs):
        raise NotImplementedError("Cannot save a project collection by client.")
