#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 rg <rg@raulgavris>
#
# Distributed under terms of the MIT license.

"""
TestController class
"""

import unittest

from application.controller import Controller
from domain.business import Plane, Passanger


class TestController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()

    def tearDown(self):
        del self.controller

    def test_plane_add_ctrl(self):
        # Plane list empty at first
        self.assertEqual(self.controller.plane_repo.planes, [])

        # Test simple add
        self.controller.plane_add_ctrl(
            name="Dummy plane name",
            number=123,
            company="alba airlines",
            seats=666,
            destination="cluj",
            passengers=[],
        )

        self.assertEqual(len(self.controller.plane_repo.planes), 1)
        self.assertEqual(self.controller.plane_repo.planes[0].name, "Dummy plane name")
        self.assertEqual(self.controller.plane_repo.planes[0].number, 123)
        self.assertEqual(self.controller.plane_repo.planes[0].company, "alba airlines")
        self.assertEqual(self.controller.plane_repo.planes[0].destination, "cluj")

        # Test add multiple planes
        for i in range(10):
            self.controller.plane_add_ctrl(
                name="Dummy plane name {}".format(i),
                number=123,
                company="alba airlines",
                seats=666,
                destination="cluj",
                passengers=[],
            )

            self.assertEqual(len(self.controller.plane_repo.planes), i + 2)

    def test_passanger_add_ctrl(self):
        # Passanger list empty at first
        self.assertEqual(self.controller.passanger_repo.passangers, [])

        # Test simple add
        self.controller.passanger_add_ctrl(
            first_name="dummy first_name",
            last_name="dummy last_name",
            passport_number=123,
        )

        self.assertEqual(len(self.controller.passanger_repo.passangers), 1)
        self.assertEqual(
            self.controller.passanger_repo.passangers[0].first_name, "dummy first_name"
        )
        self.assertEqual(
            self.controller.passanger_repo.passangers[0].last_name, "dummy last_name"
        )
        self.assertEqual(
            self.controller.passanger_repo.passangers[0].passport_number, 123
        )

        # Test add multiple passangers
        for i in range(10):
            self.controller.passanger_add_ctrl(
                first_name="dummy first_name {}".format(i),
                last_name="dummy last_name",
                passport_number=123,
            )

            self.assertEqual(len(self.controller.passanger_repo.passangers), i + 2)

    def test_plane_get_by_index_ctrl(self):
        # Plane list empty at first
        self.assertEqual(self.controller.plane_repo.planes, [])

        self.controller.plane_add_ctrl(
            name="Dummy plane name 0",
            number=123,
            company="alba airlines",
            seats=666,
            destination="cluj",
            passengers=[],
        )
        self.controller.plane_add_ctrl(
            name="Dummy plane name 1",
            number=123,
            company="alba airlines",
            seats=666,
            destination="cluj",
            passengers=[],
        )
        self.controller.plane_add_ctrl(
            name="Dummy plane name 2",
            number=123,
            company="alba airlines",
            seats=666,
            destination="cluj",
            passengers=[],
        )

        self.assertEqual(
            self.controller.plane_get_by_index_ctrl(0).name, "Dummy plane name 0"
        )
        self.assertEqual(
            self.controller.plane_get_by_index_ctrl(1).name, "Dummy plane name 1"
        )
        self.assertEqual(
            self.controller.plane_get_by_index_ctrl(2).name, "Dummy plane name 2"
        )

    def test_passanger_get_by_index_ctrl(self):
        self.assertEqual(self.controller.passanger_repo.passangers, [])

        self.controller.passanger_add_ctrl(
            first_name="dummy first_name 0",
            last_name="dummy last_name",
            passport_number=123,
        )
        self.controller.passanger_add_ctrl(
            first_name="dummy first_name 1",
            last_name="dummy last_name",
            passport_number=123,
        )
        self.controller.passanger_add_ctrl(
            first_name="dummy first_name 2",
            last_name="dummy last_name",
            passport_number=123,
        )

        self.assertEqual(
            self.controller.passanger_get_by_index_ctrl(0).first_name,
            "dummy first_name 0",
        )
        self.assertEqual(
            self.controller.passanger_get_by_index_ctrl(1).first_name,
            "dummy first_name 1",
        )
        self.assertEqual(
            self.controller.passanger_get_by_index_ctrl(2).first_name,
            "dummy first_name 2",
        )

    def test_plane_update_by_name_id_ctrl(self):
        # Plane list empty at first
        self.assertEqual(self.controller.plane_repo.planes, [])

        self.controller.plane_add_ctrl(
            name="Dummy plane name",
            number=123,
            company="alba airlines",
            seats=666,
            destination="cluj",
            passengers=[],
        )

        self.controller.plane_update_by_name_id_ctrl(
            name_id="Dummy plane name",
            name="Dummy plane name 0",
            number=123,
            company="dej airlines",
            seats=666,
            destination="cluj",
            passengers=[],
        )

        # Test previous fields are tsill the same
        self.assertEqual(len(self.controller.plane_repo.planes), 1)
        self.assertEqual(self.controller.plane_repo.planes[0].number, 123)
        self.assertEqual(self.controller.plane_repo.planes[0].company, "dej airlines")
        self.assertEqual(self.controller.plane_repo.planes[0].destination, "cluj")

        self.assertEqual(
            self.controller.plane_repo.planes[0].name, "Dummy plane name 0"
        )

    def test_passanger_update_by_name_id_ctrl(self):
        self.assertEqual(self.controller.passanger_repo.passangers, [])

        self.controller.passanger_add_ctrl(
            first_name="dummy first name",
            last_name="dummy last_name",
            passport_number=123,
        )

        self.controller.passanger_update_by_name_id_ctrl(
            name_id="dummy first name",
            first_name="dummy first_name changed",
            last_name="dummy last_name",
            passport_number=123,
        )

        # Test older fields still there
        self.assertEqual(len(self.controller.passanger_repo.passangers), 1)
        self.assertEqual(
            self.controller.passanger_repo.passangers[0].last_name, "dummy last_name"
        )
        self.assertEqual(
            self.controller.passanger_repo.passangers[0].passport_number, 123
        )

        self.assertEqual(
            self.controller.passanger_repo.passangers[0].first_name,
            "dummy first_name changed",
        )

    def test_delete_plane_by_index_ctrl(self):
        self.assertEqual(self.controller.plane_repo.planes, [])

        self.controller.plane_add_ctrl(
            name="Dummy plane name",
            number=123,
            company="alba airlines",
            seats=666,
            destination="cluj",
            passengers=[],
        )

        self.assertEqual(len(self.controller.plane_repo.planes), 1)
        self.controller.plane_delete_by_index_ctrl(0)
        self.assertEqual(len(self.controller.plane_repo.planes), 0)

    def test_delete_passanger_by_index_ctrl(self):
        self.assertEqual(self.controller.passanger_repo.passangers, [])

        self.controller.passanger_add_ctrl(
            first_name="dummy first name",
            last_name="dummy last_name",
            passport_number=123,
        )

        self.assertEqual(len(self.controller.passanger_repo.passangers), 1)
        self.controller.passanger_delete_by_index_ctrl(0)
        self.assertEqual(len(self.controller.passanger_repo.passangers), 0)

    def test_sort_passangers_by_lastname_ctrl(self):
        p = []
        for i in range(9):
            p.append(
                Passanger(
                    first_name="dummy first_name {}".format(9 - i),
                    last_name="dummy last_name {}".format(9 - i),
                    passport_number=123,
                )
            )

        self.controller.plane_add_ctrl(
            name="Dummy plane name",
            number=123,
            company="alba airlines",
            seats=666,
            destination="cluj",
            passengers=p,
        )

        self.controller.sort_passangers_by_lastname_ctrl("Dummy plane name")

        for i in range(9):
            self.assertEqual(
                self.controller.plane_repo.planes[0].passengers[i].last_name,
                "dummy last_name {}".format(i + 1),
            )

    def test_sort_planes_by_number_of_passangers_ctrl(self):
        # Add less and less passengers
        for j in range(3):
            p = []
            for i in range(9 - j):
                p.append(
                    Passanger(
                        first_name="dummy first_name {}".format(9 - i),
                        last_name="dummy last_name {}".format(9 - i),
                        passport_number=123,
                    )
                )

            self.controller.plane_add_ctrl(
                name="Dummy plane name {}".format(3 - j),
                number=123,
                company="alba airlines",
                seats=666,
                destination="cluj",
                passengers=p,
            )

        self.controller.sort_planes_by_number_of_passangers_ctrl()

        for i in range(3):
            self.assertEqual(
                self.controller.plane_repo.planes[i].name,
                "Dummy plane name {}".format(i + 1),
            )

    def test_sort_planes_by_number_of_pass_named_starting_with_ctrl(self):
        # Add less and less passengers
        for j in range(3):
            p = []
            for i in range(9 - j):
                p.append(
                    Passanger(
                        first_name="dummy first_name {}".format(9 - i),
                        last_name="dummy last_name {}".format(9 - i),
                        passport_number=123,
                    )
                )

            self.controller.plane_add_ctrl(
                name="Dummy plane name {}".format(3 - j),
                number=123,
                company="alba airlines",
                seats=666,
                destination="cluj",
                passengers=p,
            )

        self.controller.sort_planes_by_number_of_pass_named_starting_with_ctrl("Dummy")

        for i in range(3):
            self.assertEqual(
                self.controller.plane_repo.planes[i].name,
                "Dummy plane name {}".format(3 - i),
            )

    def test_find_planes_with_passangers_with_weird_passports_ctrl(self):
        for j in range(3):
            p = []
            for i in range(9 - j):
                p.append(
                    Passanger(
                        first_name="dummy first_name {}".format(9 - i),
                        last_name="dummy last_name {}".format(9 - i),
                        passport_number="111123{}".format(i),
                    )
                )

            self.controller.plane_add_ctrl(
                name="Dummy plane name {}".format(3 - j),
                number=123,
                company="alba airlines",
                seats=666,
                destination="cluj",
                passengers=p,
            )

        planes = self.controller.find_planes_with_passangers_with_weird_passports_ctrl()

        self.assertEqual(len(planes), 3)

    def test_find_passangers_from_plane_ctrl(self):
        p = []
        for i in range(9):
            p.append(
                Passanger(
                    first_name="dummy first_name {}".format(9 - i),
                    last_name="dummy last_name {}".format(9 - i),
                    passport_number=123,
                )
            )

        self.controller.plane_add_ctrl(
            name="Dummy plane name",
            number=123,
            company="alba airlines",
            seats=666,
            destination="cluj",
            passengers=p,
        )

        passengers = self.controller.find_passangers_from_plane_ctrl(
            self.controller.plane_repo.planes[0], "dummy"
        )

        self.assertEqual(len(passengers), 9)

    def test_find_planes_with_passanger_ctrl(self):
        for j in range(3):
            p = []
            for i in range(9 - j):
                p.append(
                    Passanger(
                        first_name="dummy first_name {}".format(9 - i),
                        last_name="dummy last_name {}".format(9 - i),
                        passport_number="111123{}".format(i),
                    )
                )

            self.controller.plane_add_ctrl(
                name="Dummy plane name {}".format(3 - j),
                number=123,
                company="alba airlines",
                seats=666,
                destination="cluj",
                passengers=p,
            )

        planes = self.controller.find_planes_with_passanger_ctrl(
            "dummy first_name 2 dummy last_name 2"
        )

        self.assertEqual(len(planes), 2)
