import re

pattern = re.compile(r"^1*(0|01)*$", flags=re.MULTILINE)

test_string = ("111\n"
	"000\n"
	"101\n"
	"110\n"
	"0101\n"
	"110010\n"
	"011\n"
	"1011\n"
	"0110\n"
	"1110111\n"
	"00011")

matches = pattern.finditer(test_string)

for match_num, match in enumerate(matches, start=1):
    print(f"Match {match_num} was found at {match.start()}-{match.end()}: {match.group()}")
    
    for group_num, group in enumerate(match.groups(), start=1):
        print(f"Group {group_num} found at {match.start(group_num)}-{match.end(group_num)}: {group}")
