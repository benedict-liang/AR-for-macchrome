#! /usr/bin/python

import environmentvariables_pb2
import sys

class ListEnvVar:

    @staticmethod
    def getEnvVarDict(filename, setid):
        env_variables = environmentvariables_pb2.EnvironmentVariables()

        try:
            f = open(filename, "rb")
            env_variables.ParseFromString(f.read())
            f.close()
        except IOError:
            return {}
        print env_variables
        def getSetIDDict(env_variables, setid):
            for variable_set in env_variables.variableset:
                if setid != variable_set.setid:
                    continue

                result_dict = {}

                result_dict['setid'] = variable_set.setid
                result_dict['chromedriver_path'] = variable_set.chromedriver_path
                result_dict['url_to_watch'] = variable_set.url_to_watch

                return result_dict

            return {}
        return getSetIDDict(env_variables, setid)
