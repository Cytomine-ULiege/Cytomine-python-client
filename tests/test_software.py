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

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import pytest

from cytomine.models import (
    Job,
    JobCollection,
    JobParameter,
    JobParameterCollection,
    Software,
    SoftwareCollection,
    SoftwareParameter,
    SoftwareParameterCollection,
    SoftwareProject,
    SoftwareProjectCollection,
)
from tests.conftest import random_string


class TestSoftware:
    @pytest.mark.skip()
    def test_software(self, connect, dataset):  # pylint: disable=unused-argument
        name = random_string()
        software = Software(name, "ValidateAnnotation").save()
        assert isinstance(software, Software)
        assert software.name == name

        software = Software().fetch(software.id)
        assert isinstance(software, Software)
        assert software.name == name

        name = random_string()
        software.name = name
        software.update()
        assert isinstance(software, Software)
        assert software.name == name

        software.delete()
        assert not Software().fetch(software.id)

    @pytest.mark.skip()
    def test_softwares(self, connect, dataset):  # pylint: disable=unused-argument
        softwares = SoftwareCollection().fetch()
        assert isinstance(softwares, SoftwareCollection)

        softwares = SoftwareCollection()
        softwares.append(Software(random_string(), "ValidateAnnotation"))
        assert softwares.save()

    @pytest.mark.skip()
    def test_softwares_by_project(
        self,
        connect,  # pylint: disable=unused-argument
        dataset,
    ):
        softwares = SoftwareCollection().fetch_with_filter(
            "project",
            dataset["project"].id,
        )
        assert isinstance(softwares, SoftwareCollection)


class TestSoftwareProject:
    @pytest.mark.skip()
    def test_software_project(
        self,
        connect,  # pylint: disable=unused-argument
        dataset,
    ):
        sp = SoftwareProject(dataset["software"].id, dataset["project"].id).save()
        assert isinstance(sp, SoftwareProject)
        assert sp.software == dataset["software"].id

        sp = SoftwareProject().fetch(sp.id)
        assert isinstance(sp, SoftwareProject)
        assert sp.software == dataset["software"].id

        sp.delete()
        assert not SoftwareProject().fetch(sp.id)

    @pytest.mark.skip()
    def test_software_projects(
        self,
        connect,  # pylint: disable=unused-argument
        dataset,  # pylint: disable=unused-argument
    ):
        sps = SoftwareProjectCollection().fetch()
        assert isinstance(sps, SoftwareProjectCollection)

    @pytest.mark.skip()
    def test_software_projects_by_project(
        self,
        connect,  # pylint: disable=unused-argument
        dataset,
    ):
        sps = SoftwareProjectCollection().fetch_with_filter(
            "project",
            dataset["project"].id,
        )
        assert isinstance(sps, SoftwareProjectCollection)


class TestSoftwareParameter:
    @pytest.mark.skip()
    def test_software_parameter(
        self,
        connect,  # pylint: disable=unused-argument
        dataset,
    ):
        name = random_string()
        sp = SoftwareParameter(
            name,
            "Number",
            dataset["software"].id,
            0,
            False,
            100,
            False,
        ).save()
        assert isinstance(sp, SoftwareParameter)
        assert sp.name == name

        sp = SoftwareParameter().fetch(sp.id)
        assert isinstance(sp, SoftwareParameter)
        assert sp.name == name

        name = name + "bis"
        sp.name = name
        sp.update()
        assert isinstance(sp, SoftwareParameter)
        assert sp.name == name

        sp.delete()
        assert not SoftwareParameter().fetch(sp.id)

    @pytest.mark.skip()
    def test_software_parameters(
        self,
        connect,  # pylint: disable=unused-argument
        dataset,
    ):
        sps = SoftwareParameterCollection()
        sps.append(
            SoftwareParameter(
                random_string(),
                "Number",
                dataset["software"].id,
                0,
                False,
                100,
                False,
            )
        )
        assert sps.save()

    @pytest.mark.skip()
    def test_software_parameters_by_software(
        self,
        connect,  # pylint: disable=unused-argument
        dataset,
    ):
        sps = SoftwareParameterCollection().fetch_with_filter(
            "software",
            dataset["software"].id,
        )
        assert isinstance(sps, SoftwareParameterCollection)


class TestJob:
    @pytest.mark.skip()
    def test_job(self, connect, dataset):  # pylint: disable=unused-argument
        job = Job(dataset["project"].id, dataset["software"].id).save()
        assert isinstance(job, Job)
        assert job.project == dataset["project"].id

        job = Job().fetch(job.id)
        assert isinstance(job, Job)
        assert job.project == dataset["project"].id

        comment = "comment"
        job.statusComment = comment
        job.update()
        assert isinstance(job, Job)
        assert job.statusComment == comment

        job.delete()
        assert not Job().fetch(job.id)

    @pytest.mark.skip()
    def test_jobs(self, connect, dataset):  # pylint: disable=unused-argument
        jobs = JobCollection(
            project=dataset["project"].id,
            software=dataset["software"].id,
        ).fetch()
        assert isinstance(jobs, JobCollection)


class TestJobParameter:
    @pytest.mark.skip()
    def test_job_parameter(self, connect, dataset):  # pylint: disable=unused-argument
        value = 10
        job_parameter = JobParameter(
            dataset["job"].id,
            dataset["software_parameter"].id,
            value,
        ).save()
        assert isinstance(job_parameter, JobParameter)
        assert int(job_parameter.value) == value

        job_parameter = JobParameter().fetch(job_parameter.id)
        assert isinstance(job_parameter, JobParameter)
        assert int(job_parameter.value) == value

        value += 3
        job_parameter.value = value
        job_parameter.update()
        assert isinstance(job_parameter, JobParameter)
        assert int(job_parameter.value) == value

        job_parameter.delete()
        assert not JobParameter().fetch(job_parameter.id)

    @pytest.mark.skip()
    def test_job_parameters(self, connect, dataset):  # pylint: disable=unused-argument
        job_parameters = JobParameterCollection().fetch_with_filter(
            "job",
            dataset["job"].id,
        )
        assert isinstance(job_parameters, JobParameterCollection)

        job_parameters = JobParameterCollection()
        job_parameters.append(
            JobParameter(dataset["job"].id, dataset["software_parameter"].id, 10)
        )
        assert job_parameters.save()


class TestJobTemplate:
    pass


class TestJobData:
    pass
