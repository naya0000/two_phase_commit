import os.path
import tempfile
import unittest

import grpc
import worker
import coordinator
import persistent_log

import twophase_pb2
import twophase_pb2_grpc

import test_util

class OneCoordinatorTest(test_util.TestBase):
    def test_set_one_value(self):
        for num_workers in range(1,6):
            self.start_coordinator_and_workers(num_workers)
            self.do_set_value('ValueA')
            self.check_values('ValueA')
            # self.recover_workers()
            # self.check_values('ValueA')
            # self.recover_coordinator()
            # self.check_values('ValueA')

    # def test_change_values(self):
    #     for num_workers in range(1, 6):
    #         self.start_coordinator_and_workers(num_workers)
    #         self.do_set_value('ValueA')
    #         self.check_values('ValueA')
    #         self.do_set_value('ValueB')
    #         self.check_values('ValueB')
    #         self.do_set_value('ValueC')
    #         self.check_values('ValueC')
    #         self.do_set_value('ValueD')
    #         self.check_values('ValueD')
    #         self.do_set_value('ValueE')
    #         self.check_values('ValueE')
    #         self.recover_workers()
    #         self.check_values('ValueE')
    #         self.do_set_value('ValueA')
    #         self.check_values('ValueA')
    #         self.recover_workers()
    #         self.check_values('ValueA')
    
    # def test_change_values_with_consistent_transitions(self):
    #     for num_workers in range(1, 6):
    #         self.start_coordinator_and_workers(num_workers)
    #         self.do_set_value('ValueA')
    #         self.check_values('ValueA')
    #         self.do_set_value('ValueB', expect_transition_from='ValueA')
    #         self.check_values('ValueB')
    #         self.do_set_value('ValueC', expect_transition_from='ValueB')
    #         self.check_values('ValueC')
    #         self.do_set_value('ValueD', expect_transition_from='ValueC')
    #         self.check_values('ValueD')
    #         self.do_set_value('ValueE', expect_transition_from='ValueD')
    #         self.check_values('ValueE')
    #         self.recover_workers()
    #         self.check_values('ValueE')
    #         self.do_set_value('ValueA', expect_transition_from='ValueE')
    #         self.check_values('ValueA')
    #         self.recover_workers()
    #         self.check_values('ValueA')

if __name__ == '__main__':
    unittest.main(verbosity=2)
