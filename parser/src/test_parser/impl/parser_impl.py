from json import dumps
from os import listdir
from os import mkdir
from os.path import exists
from os.path import isfile
from os.path import join
from typing import AnyStr
from typing import List
from typing import Optional
from uuid import uuid4

from test_parser.const import DEFAULT_CORRECT_OPTION_PREFIX
from test_parser.const import DEFAULT_OUT_FILE_NAME
from test_parser.const import DEFAULT_QUESTION_BLOCK_SEP
from test_parser.const import DEFAULT_TESTS_COLLECTION_NAME
from test_parser.const import DEFAULT_WRONG_OPTION_PREFIX
from test_parser.model import Question


class ParserImpl:

    def __init__(self, res_src_dir: AnyStr, res_out_dir: AnyStr):
        self._res_src_dir = res_src_dir
        self._res_out_dir = res_out_dir


    def parse_tests(self) -> None:
        test_files = [join(self._res_src_dir, file) for file in listdir(self._res_src_dir)
                      if isfile(join(self._res_src_dir, file))]

        questions = self._read_each_question_block(test_files)
        self._parse_to_json(questions)


    @staticmethod
    def _read_each_question_block(test_files: List[AnyStr]) -> List[Question]:
        questions_blocks: List[Question] = []

        for file in test_files:
            with open(file, mode = 'r', encoding = 'UTF-8') as file:
                q: Optional[Question] = None

                for line in file:
                    line = line.replace('\n', '')
                    try:
                        if line.startswith(DEFAULT_WRONG_OPTION_PREFIX):
                            q.add_wrong_option(line.strip())
                        elif line.startswith(DEFAULT_CORRECT_OPTION_PREFIX):
                            line = line.replace(DEFAULT_CORRECT_OPTION_PREFIX, '').strip()
                            q.add_correct_option(line)
                        elif len(line.strip()) > 0 and q is None:
                            q = Question(line.strip())
                        elif line.strip() == DEFAULT_QUESTION_BLOCK_SEP:
                            questions_blocks.append(q)
                            q = None
                    except AttributeError:
                        continue

        return questions_blocks


    def _parse_to_json(self, questions: List[Question]) -> None:
        if not exists(self._res_out_dir):
            mkdir(self._res_out_dir)

        parsed_qs = [q.to_dict() for q in questions]

        structure = {
          "Id":        str(uuid4()),
          "Name":      DEFAULT_TESTS_COLLECTION_NAME,
          "Questions": parsed_qs
        }
        json = dumps(structure, indent = 0)

        filepath = join(self._res_out_dir, DEFAULT_OUT_FILE_NAME)
        with open(filepath, mode = 'w', encoding = 'UTF-8') as file:
            file.writelines(json)
