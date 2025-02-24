#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import pytest
import logging

from nomad.datamodel import EntryArchive

from exampleparser import ExampleParser


@pytest.fixture
def parser():
    return ExampleParser()


def test_example(parser):
    archive = EntryArchive()
    parser.parse('tests/data/example.out', archive, logging)

    run = archive.section_run[0]
    assert len(run.section_system) == 2
    assert len(run.section_single_configuration_calculation) == 2
    assert run.section_single_configuration_calculation[0].x_example_magic_value == 42
