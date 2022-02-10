# -*- coding: utf-8 -*-

# * Copyright (c) 2009-2018. Authors: see NOTICE file.
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

from cytomine.cytomine import Cytomine

__author__ = "Rubens Ulysse <urubens@uliege.be>"
__contributors__ = ["Marée Raphaël <raphael.maree@uliege.be>", "Mormont Romain <r.mormont@uliege.be>"]
__copyright__ = "Copyright 2010-2018 University of Liège, Belgium, http://www.cytomine.be/"

from cytomine.models.collection import Collection
from cytomine.models.model import Model


class Ontology(Model):
    """
    Class representing an ontology.
    """

    def __init__(self, name=None, **attributes):
        """
        Initialize an Ontology object.

        Parameters
        ----------
        name : str
            The name of the ontology.
        attributes : dict
            Other parameters.
        """
        super(Ontology, self).__init__()
        self.name = name
        self.user = None
        self.title = None
        self.attr = None
        self.data = None
        self.isFolder = None
        self.key = None
        self.children = None
        self.populate(attributes)


class OntologyCollection(Collection):
    """
    Class representing a collection of ontologies.
    """

    def __init__(self, filters=None, max=0, offset=0, **parameters):
        """
        Initialize the OntologyCollection object.

        Parameters
        ----------
        filters : dict, default=None
            The filters to apply on the collection.
        max : int, default=0
            The number of maximum items to fetch in one request.
        offset : int, default=0
            The offset for the next page.
        parameters : dict
            Other parameters.
        """
        super(OntologyCollection, self).__init__(Ontology, filters, max, offset)
        self._allowed_filters = [None]
        self.set_parameters(parameters)


class Term(Model):
    """
    Class representing a term.
    """

    def __init__(self, name=None, id_ontology=None, color=None, id_parent=None, **attributes):
        """
        Initialize a Term object.

        Parameters
        ----------
        name : str, default=None
            The name of the term.
        id_ontology : int, default=None
            The ID of the ontology associated to this term.
        color : str, default=None
            The color associated to this term in HTML format.
        id_parent : int, default=None
            The ID of the parent term if there is one.
        attributes : dict
            Other parameters.
        """
        super(Term, self).__init__()
        self.name = name
        self.ontology = id_ontology
        self.parent = id_parent
        self.color = color
        self.populate(attributes)


class TermCollection(Collection):
    """
    Class representing a collection of terms.
    """

    def __init__(self, filters=None, max=0, offset=0, **parameters):
        """
        Initialize a TermCollection object.

        Parameters
        ----------
        name : str, default=None
            The name of the term.
        max : int, default=0
            The number of maximum items to fetch in one request.
        offset : int, default=0
            The offset for the next page.
        parameters : dict
            Other parameters.
        """
        super(TermCollection, self).__init__(Term, filters, max, offset)
        self._allowed_filters = [None, "project", "ontology", "annotation"]
        self.set_parameters(parameters)


class RelationTerm(Model):
    """
    Class representing a relation between two terms.
    """

    def __init__(self, id_term1=None, id_term2=None, **attributes):
        """
        Initialize a RelationTerm object.

        Parameters
        ----------
        id_term1 : int, default=None
            The ID of the first term.
        id_term2 : int, default=None
            The ID of the second term.
        attributes : dict
            Other parameters.
        """
        super(RelationTerm, self).__init__()
        self.term1 = id_term1
        self.term2 = id_term2
        self.populate(attributes)

    def uri(self):
        if not self.id:
            return "relation/parent/term.json"
        else:
            return "relation/parent/term1/{}/term2/{}.json".format(self.term1, self.term2)

    def fetch(self, id_term1=None, id_term2=None):
        self.id = -1

        if self.term1 is None and id_term1 is None:
            raise ValueError("Cannot fetch a model with no term 1 ID.")
        elif self.term2 is None and id_term2 is None:
            raise ValueError("Cannot fetch a model with no term 2 ID.")

        if id_term1 is not None:
            self.term1 = id_term1

        if id_term2 is not None:
            self.term2 = id_term2

        return Cytomine.get_instance().get_model(self, self.query_parameters)

    def update(self, *args, **kwargs):
        raise NotImplementedError("Cannot update a relation-term.")

    def __str__(self):
        return "[{}] {} : parent {} - child {}".format(self.callback_identifier, self.id, self.term1, self.term2)
