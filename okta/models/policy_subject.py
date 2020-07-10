"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from okta.okta_object import OktaObject


class PolicySubject(
    OktaObject
):
    def __init__(self, config=None):
        if config:
            self.filter = config["filter"]\
                if "filter" in config else None
            self.format = config["format"]\
                if "format" in config else None
            self.match_attribute = config["matchAttribute"]\
                if "matchAttribute" in config else None
            self.match_type = config["matchType"]\
                if "matchType" in config else None
            self.user_name_template = config["userNameTemplate"]\
                if "userNameTemplate" in config else None
        else:
            self.filter = None
            self.format = None
            self.match_attribute = None
            self.match_type = None
            self.user_name_template = None
