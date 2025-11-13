import random
import time
import string
import turtle as t
from time import sleep

text = """ThereareyouIandletlistintgameJupiterlinedefblindasyieldassertbreakclasscontinueexceptfinallyforfromglobalimportnonlocalpassraisereturntrywhilewithandorasassertbreakclasscontinuedefdelelifelseexceptexecfinallyforfromglobalifimportinislambdnonlocalnotorpassprintraisereprreturnsupertrywhilewithyieldTrueFalseNoneasyncawaitmatchcasenonelocaloverrideprivatesealedstaticmethodvolatileabstractenumintfloatdoublebyteboolcharstructvectorlistdictionaryqueuestackinterfacenulltrycatchfinallythrowthrowsimplementsextendspublicprotectedprivatefinalstaticvoidmainStringargsSystemoutprintlnnewMapSetGetAddRemoveClearIsEmptySizeContainsKeyContainsValueKeyValuePairsForEachDoWhileSwitchCaseDefaultbreakcontinueiteratoriterablecollectionsframeworksynchronizedtransientvolatilestrictfpbitwiselogicalshiftcompoundassignmenttypeinferencegenericswildcardstypeerasurereflectionproxydecoratorfactorysingletonprototypebuildercompositeadapterbridgechainofresponsibilitycommandstateobservermementointerpreteriteratorvisitorstrategytemplatemethodflyweightmediatorproxymultithreadingconcurrencyasynchronousprogrammingeventdrivenarchitecturefunctionalprogrammingimmutables...

quantumcomputingqubitsentanglementsuperpositionquantumalgorithmsShorsGroverquantumcryptographyquantumteleportationartificialintelligenceAIoptimizationalgorithmsgraphtheorytraversalsearchalgorithmsdepthfirstsearchbreadthfirstsearchAstaralgorithmgeneticalgorithmssimulatedannealingparticlewarmoptimizationantcolonyoptimizationmachinelearningdeeplearningunsupervisedlearningreinforcementlearningneuralnetworksconvolutionalneuralnetworksrecurrentneuralnetworkslongshorttermmemorynetworksgenerativeadversar...

blockchaintechnologydistributedledgerconsensusalgorithmsproofOfWorkproofOfStakeByzantineFaultTolerancepeer-to-peerP2PnetworkscryptographyhashfunctionsasymmetricencryptionpublickeyinfrastructurePKIdigitalcertificatesdigital signaturesmartcontractsdecentralizedapplicationsDAppsEthereumplatformSolidityprogramminglanguageWeb3technologyNFTsnon-fungibletokensDeFidecentralizedfinancedecentralizedexchangesDEXsstablecoinscryptocurrencyminingstakingyieldfarmingliquiditypoolsoraclesDAOsdecentralizedautonomousorganizati..."""


def decrypt_clue(text):
    keyword_py = (
        "and", "for", "false", "as", "assert", "none", "true", "async", "await", "break", "class", "continue", "def",
        "del",
        "elif", "else", "except", "finally", "from", "global",
        "if", "import", "in", "is", "iambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while",
        "with",
        "yeild")
    my_list = []
    for i in keyword_py:
        my_list.append(i)
    return my_list


a_1 = decrypt_clue(text)

print("\n")


def solve_puzzles(puzzles):
    rst = []

    for m in puzzles:
        if isinstance(m, int) or isinstance(m, float):
            if m != 0:
                rst.append('True')
            else:
                rst.append('False')
        elif isinstance(m, str) or isinstance(m, list) or isinstance(m, set) or isinstance(m, dict):
            if len(m) != 0:
                rst.append('True')
            else:
                rst.append('False')
        elif m == None:
            rst.append('False')
        else:
            if m == True:
                rst.append('True')
            else:
                rst.append('False')

    return rst


puzzles = ['ali', 1233, 0, "", [], {}, 'False', '0', 'None', None, -1, [1, 2, 3], {'key': 'value'}, True, ' ', '[]',
           '[1, 2, 3]', '{}', '{"a": 1}', 'True', 'ali', '1234', 1, 0.1, -0.1, True, ' ', '[]', '[1, 2, 3]', '{}',
           '{"a": 1}', 'True', 'ali', '1234', 1, 0.1, -0.1, True, ' ', '[]', '[1, 2, 3]', '{}', '{"a": 1}', 'True',
           'ali', '1234', 1, 0.1, -0.1]

a_2 = puzzles

print("\n")


def calculate_magic_numbers(start, end):
    x = 0.3
    x = x * ((end - start) + start)
    return x


a_3_1 = str(calculate_magic_numbers(1, 20))


def exam_numbers_(random_bin):
    return int(random_bin, 2)
def exam_numbers():
    correct_answers = 0
    wrong_answers = 0

    print("you only have 20 seconds for enter decimal num")
    start_time = time.perf_counter()
    random_bin = "{:04b}".format(random.randint(0, 10))
    answer = []
    while True:
        if correct_answers > 0:
            random_bin = "{:04b}".format(random.randint(0, 10))

        x_input = int(input(f"Enter the decimal num of {random_bin}: "))

        if x_input == exam_numbers_(random_bin):
            correct_answers += 1
            print("Correct(:")
            answer.append('True')
        else:
            wrong_answers += 1
            print("Wrong!")
            answer.append('False')
        end_time = time.perf_counter()
        if end_time - start_time >= 20:
            break
        else:
            print("Number of correct answers:", correct_answers)
            print("Number of wrong answers:", wrong_answers)
    return answer


a_3_2 = exam_numbers()


def check_pass():
    user_password = input("Enter password: ")
    while True:

        if len(user_password) != 8:
            print("Password must be 8 characters.")
        elif user_password:
            characters = string.punctuation
            digits = string.digits
            words = string.ascii_lowercase + string.ascii_uppercase

            print("the pass is correct.")
            return "correct"
        else:
            print("conditions must be met.")
            return "Wrong"


a_3_3 = check_pass()
a_3 = a_3_1[0] + a_3_2[0][0] + a_3_3[0][0]
print("\n")


def unlock_vault(a1, a2, a3, a4="lataragi"):
    a_1_f = str(a1[0][0])
    a_2_f = str(a2[0][0])
    a_3_f = str(a3)
    a_4_f = str(a4[0])
    vault = a_1_f + a_2_f + a_3_f + a_4_f
    print(vault)


unlock_vault(a_1, a_2, a_3)