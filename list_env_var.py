#! /usr/bin/python

import environmentvariables_pb2
import sys

class ListEnvVar:

    def getEnvVarDict(filename, setid):
        env_variables = environmentvariables_pb2.EnvironmentVariables()

        try:
            f = open(filename, "rb")
            env_variables.ParseFromString(f.read())
            f.close()
        except IOError:
            return {}

        return __getSetIDDict(env_variables, setid)

    def __getSetIDDict(env_variables, setid):
        for variable_set in env_variables:
            if setid != variable_set.setid:
                continue

            result_dict = {}

            result_dict['setid'] = variable_set.setid
            result_dict['chromedriver_path'] = variable_set.chromedriver_path
            result_dict['url_to_watch'] = variable_set.url_to_watch

            return result_dict

        return {}
