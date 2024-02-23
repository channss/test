import time
import pandas as pd
import random

def elapsed(original_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()
        print(f'{end - start} seconds')
        return result

    return wrapper

@elapsed
def dict_finder(dict, key):
    if key in dict:
        print(f'{key} found!')
        return
    print(f'{key} not found!')
    return

@elapsed
def df_finder(df, key):
    if df[df['column1'] == key].empty:
        print(f'{key} not found!')
        return
    print(f'{key} found!')
    return

my_dictionary = {
    'ohlfngbhoj': (9, 'zxcv'),
    'voclenzwis': (9, 'asdf'),
    'xqxzoshaar': (2, 'zxcv'),
    'jowtfxmkfb': (10, 'asdf'),
    'naucxnizdo': (7, 'zxcv'),
    'fanpqkrzhv': (0, 'asdf'),
    'lkhwgfgnna': (9, 'asdf'),
    'lbrzlezivi': (0, 'asdf'),
    'fougutnjcr': (8, 'qwer'),
    'evxqumwkaw': (6, 'qwer'),
    'agjwlgfxmk': (7, 'asdf'),
    'ijliihhpdv': (9, 'qwer'),
    'wivhpxuazc': (0, 'qwer'),
    'xzqoblkbml': (2, 'qwer'),
    'ounpigwrcn': (8, 'zxcv'),
    'teaflvvmcr': (7, 'qwer'),
    'njlinifdvm': (8, 'qwer'),
    'nljdemksim': (0, 'zxcv'),
    'zixfqerluj': (7, 'asdf'),
    'dywnevxvdx': (4, 'asdf'),
    'mnxdafoaqp': (6, 'asdf'),
    'utmrnwuacm': (5, 'qwer'),
    'nntbiqdgnq': (0, 'asdf'),
    'yylzgzhdia': (5, 'qwer'),
    'dyyxqhjzuh': (4, 'zxcv'),
    'emosxrqiiy': (7, 'qwer'),
    'nawxulyhgq': (8, 'zxcv'),
    'wsobddlrlt': (6, 'zxcv'),
    'bsstteizgs': (4, 'zxcv'),
    'ncebxmvjxh': (3, 'zxcv'),
    'igqwwqledw': (8, 'qwer'),
    'eryjewfaji': (7, 'qwer'),
    'ihcuhnrlsu': (6, 'asdf'),
    'bpbiolwpzv': (1, 'qwer'),
    'xtrkrqhknm': (7, 'zxcv'),
    'uyprnzbquk': (7, 'qwer'),
    'dzundmhqke': (1, 'asdf'),
    'nbcglpuwse': (7, 'zxcv'),
    'teonaubwcq': (6, 'qwer'),
    'pnbfwdrckz': (6, 'qwer'),
    'vtdmhmqkzx': (2, 'asdf'),
    'jvclnoferq': (4, 'zxcv'),
    'gnjdejetio': (8, 'qwer'),
    'qjqntjfbbx': (0, 'asdf'),
    'ohopwqfwfw': (7, 'zxcv'),
    'qsmkdajkbs': (3, 'zxcv'),
    'qacgjnbbnq': (8, 'qwer'),
    'nohdiqufyw': (10, 'qwer'),
    'quymhhqswi': (7, 'asdf'),
    'oyymnvenft': (7, 'qwer'),
    'ezupoommbc': (5, 'qwer'),
    'caryfppfvd': (4, 'asdf'),
    'mgoqqzhxlw': (6, 'asdf'),
    'yunntllaoq': (6, 'zxcv'),
    'mshxbqvpyd': (10, 'qwer'),
    'dsxhrjcqay': (1, 'zxcv'),
    'mxikvckynx': (3, 'asdf'),
    'sezjmkpdbq': (8, 'asdf'),
    'vewyjelfmp': (8, 'qwer'),
    'gpnpotijtp': (3, 'qwer'),
    'ezdkfezwxs': (7, 'qwer'),
    'mgjmlhhrwq': (5, 'zxcv'),
    'khtbniuoum': (1, 'qwer'),
    'bornogduxw': (0, 'zxcv'),
    'lkkovzoaak': (4, 'asdf'),
    'vwslhcouil': (3, 'qwer'),
    'pvwdbmbved': (8, 'asdf'),
    'ysxoyaeecg': (3, 'zxcv'),
    'cnvceohldi': (5, 'qwer'),
    'ezwjbmezau': (6, 'asdf'),
    'hvfkogvqdd': (0, 'asdf'),
    'zozlwfbnbr': (3, 'zxcv'),
    'iljnavdjnr': (5, 'asdf'),
    'waonryhije': (8, 'asdf'),
    'gjlgvyxexr': (9, 'qwer'),
    'dnvzcyxwcd': (8, 'zxcv'),
    'vvkpdbhher': (9, 'zxcv'),
    'kapdebjyck': (10, 'asdf'),
    'jvkbuzjfri': (2, 'zxcv'),
    'fcjfimfmyl': (10, 'qwer'),
    'eonrdrwged': (9, 'asdf'),
    'tfqplfhdkx': (7, 'qwer'),
    'txtgvjadqd': (8, 'asdf'),
    'funquqovhm': (2, 'zxcv'),
    'qetqsdpbnb': (2, 'asdf'),
    'tsivybbgqw': (0, 'zxcv'),
    'zrenvuqefn': (4, 'asdf'),
    'dynkbyubbv': (6, 'qwer'),
    'vycmyttjog': (0, 'qwer'),
    'ozembizyne': (3, 'asdf'),
    'psmhudnrnk': (9, 'zxcv'),
    'lzdlmjnibz': (8, 'zxcv'),
    'wjflsmxdws': (6, 'asdf'),
    'berndbslnf': (10, 'qwer'),
    'kmaoekwprg': (5, 'zxcv'),
    'gpsodfgses': (8, 'qwer'),
    'qujrefuhwt': (7, 'asdf'),
    'cvgawlmtbk': (9, 'qwer'),
    'ifrfnybcmp': (8, 'qwer'),
    'nmdaacharh': (3, 'qwer'),
    'ijeydfmkss': (7, 'qwer'),
    'wxqgkosfdu': (10, 'asdf'),
    'pvrkxjqopq': (7, 'asdf'),
    'yugimryrtk': (3, 'asdf'),
    'uvqifjehpa': (0, 'zxcv'),
    'csuozgeolw': (10, 'qwer'),
    'bijhnvymfo': (2, 'asdf'),
    'jjtsyeignv': (8, 'qwer'),
    'ftfosxikld': (1, 'asdf'),
    'miykrxbgto': (2, 'asdf'),
    'upbgyrupsn': (0, 'asdf'),
    'eqlyqmwidb': (2, 'asdf'),
    'ptuijhapsa': (1, 'zxcv'),
    'ihghqwkycb': (6, 'qwer'),
    'dbqiypcggz': (4, 'zxcv'),
    'shgwvmulku': (7, 'zxcv'),
    'rifyugoakv': (5, 'zxcv'),
    'qwdlqqffrr': (5, 'zxcv'),
    'jsmsaudwoc': (1, 'qwer'),
    'nnljzqdkro': (7, 'asdf'),
    'ckdyjbeelj': (4, 'qwer'),
    'quenwtprlq': (4, 'qwer'),
    'tctwpmuvri': (3, 'zxcv'),
    'cirlpnjsyx': (1, 'zxcv'),
    'iegpwpxlei': (10, 'asdf'),
    'iitoclmikc': (0, 'zxcv'),
    'qtxeiwmgut': (5, 'asdf'),
    'nzjuydazbt': (5, 'zxcv'),
    'rrasrbxhjz': (7, 'zxcv'),
    'pzddwnmwxb': (1, 'qwer'),
    'qnipzgqxcx': (7, 'qwer'),
    'ajlpkipcrf': (0, 'qwer'),
    'cqwkjiczvn': (2, 'asdf'),
    'xwdplagvon': (5, 'qwer'),
    'dnciyscims': (0, 'qwer'),
    'hyggtqgebm': (5, 'qwer'),
    'lnmlkqjrld': (2, 'asdf'),
    'atpdniepng': (1, 'qwer'),
    'yshiwozbgo': (2, 'asdf'),
    'mvehjdxpbz': (10, 'zxcv'),
    'wyrxtcygar': (3, 'zxcv'),
    'lqypbzzonq': (5, 'asdf'),
    'fporksxgfx': (5, 'qwer'),
    'sjhwbzpfli': (0, 'asdf'),
    'pntxkturpr': (2, 'qwer'),
    'pkbgubvebe': (1, 'asdf'),
    'ysjbrkizej': (7, 'asdf'),
    'edyldvexmh': (7, 'asdf'),
    'izmauknxww': (6, 'zxcv'),
    'csgpurjyqz': (10, 'qwer'),
    'ukiogbtbkk': (9, 'qwer'),
    'llcxfguzot': (10, 'asdf'),
    'pbkfdmkufb': (9, 'asdf'),
    'axtpfktzth': (2, 'asdf'),
    'dqsnkbegpn': (6, 'asdf'),
    'opmpfjztzg': (10, 'asdf'),
    'bgneypqdea': (8, 'zxcv'),
    'sjrhtwrtxc': (8, 'asdf'),
    'smdzfwmvva': (9, 'asdf'),
    'ojavnmfgdr': (7, 'qwer'),
    'hafsjnvwgg': (7, 'asdf'),
    'kdxactrbvl': (10, 'qwer'),
    'xecnuysqfu': (9, 'qwer'),
    'ounvwrjqrx': (4, 'zxcv'),
    'ebccudiurc': (9, 'zxcv'),
    'yvtlcwiulm': (1, 'zxcv'),
    'fyacawzuim': (1, 'zxcv'),
    'bqczmpetwi': (2, 'zxcv'),
    'enwtvhyqtz': (10, 'zxcv'),
    'mxwznmanfb': (3, 'qwer'),
    'hwsbusgyfz': (3, 'zxcv'),
    'pxvmmtefol': (0, 'zxcv'),
    'qburelhwkm': (1, 'qwer'),
    'jrrzvsguwb': (5, 'qwer'),
    'ztljffgprc': (10, 'zxcv'),
    'wgktfwobiz': (9, 'qwer'),
    'estonljmoj': (5, 'zxcv'),
    'vzoccaybvi': (7, 'qwer'),
    'xsxpthzsei': (9, 'zxcv'),
    'xlapjufocd': (3, 'asdf'),
    'ryvplxvpkr': (8, 'asdf'),
    'vxdxqbvoqy': (8, 'asdf'),
    'fyswhamtjb': (6, 'zxcv'),
    'prafenuasd': (2, 'zxcv'),
    'rdgmrcklvf': (5, 'asdf'),
    'sxtcjvrqbm': (6, 'zxcv'),
    'inrvjytdpe': (1, 'asdf'),
    'ouvasngfpz': (2, 'asdf'),
    'tceamqlnjp': (0, 'qwer'),
    'ulebepwufp': (3, 'zxcv'),
    'mqfbnyhjvf': (7, 'qwer'),
    'ccsjtulywm': (10, 'zxcv'),
    'jbebupaaxg': (10, 'qwer'),
    'suohlzbifg': (5, 'asdf'),
    'rlqtkbxpof': (6, 'zxcv'),
    'dacfywcicp': (3, 'zxcv'),
    'zyssgeykop': (9, 'asdf'),
    'cdgqlzifmg': (9, 'zxcv'),
    'owfokkgyrp': (9, 'asdf'),
    'suqodotvko': (8, 'qwer'),
    'lnukzinypv': (3, 'asdf'),
    'hkdqtsgjtx': (1, 'asdf'),
    'novcrmescv': (1, 'asdf'),
    'dtmptguwwd': (9, 'asdf'),
    'qbcdaucdgq': (5, 'zxcv'),
    'qhecyqpykk': (2, 'qwer'),
    'hnlnjfvemq': (9, 'qwer'),
    'xuqybwmobt': (5, 'zxcv'),
    'nhlnvgtgdw': (3, 'qwer'),
    'lygrgfaieg': (1, 'asdf'),
    'rhodxskykg': (6, 'asdf'),
    'vxccpltkze': (10, 'asdf'),
    'zzschzjfgx': (10, 'zxcv'),
    'dbsmxnednk': (0, 'qwer'),
    'wxmemxdwhd': (2, 'asdf'),
    'ydssvrnexp': (7, 'asdf'),
    'eyrvgidmwp': (4, 'zxcv'),
    'vxjqaxgrrv': (3, 'asdf'),
    'ujteedxwwu': (0, 'asdf'),
    'yehdttzgpu': (9, 'qwer'),
    'hdteffjtlo': (1, 'asdf'),
    'ezzeadjkqn': (0, 'qwer'),
    'hzhcwwvgdq': (10, 'zxcv'),
    'olbjpddcrf': (9, 'qwer'),
    'xlixgfmtml': (0, 'zxcv'),
    'jykwlleyef': (10, 'qwer'),
    'lupbvqrwtm': (3, 'asdf'),
    'gxtaptcnvv': (4, 'asdf'),
    'fboadztrhc': (5, 'qwer'),
    'vnbhyjbqms': (7, 'asdf'),
    'hnydjnzddp': (10, 'asdf'),
    'nmrnnctrrp': (6, 'asdf'),
    'lxnqftnzsx': (6, 'qwer'),
    'wkxxkdefry': (9, 'asdf'),
    'uxalntlfyr': (2, 'qwer'),
    'yglgvhpbye': (10, 'asdf'),
    'tedtfcjzot': (9, 'qwer'),
    'fkbndldhpu': (5, 'qwer'),
    'rfkzwnpxju': (2, 'asdf'),
    'iolzkelnws': (5, 'zxcv'),
    'vrvlymkaij': (3, 'zxcv'),
    'dnlitiyvgk': (10, 'asdf'),
    'rtvuqjynwd': (10, 'qwer'),
    'lbwmimpfhe': (10, 'qwer'),
    'grdzeqzunh': (7, 'qwer'),
    'wcefpaizoh': (5, 'qwer'),
    'iuhwcjqmbp': (4, 'asdf'),
    'juvilwykkp': (0, 'zxcv'),
    'fbjjdynqem': (7, 'asdf'),
    'ammuvzcwkx': (7, 'qwer'),
    'hgudcrtkev': (8, 'qwer'),
    'tqkiomqkaw': (0, 'qwer'),
    'grcyuleylz': (3, 'qwer'),
    'dgzixobbez': (0, 'zxcv'),
    'dpyslxrsdo': (8, 'zxcv'),
    'dinmgnshkh': (3, 'zxcv'),
    'newfkznodt': (8, 'zxcv'),
    'rbzlpgioxb': (0, 'qwer'),
    'vnkqqalkym': (0, 'zxcv'),
    'ifqupdytsa': (9, 'qwer'),
    'sdymdycgzs': (1, 'zxcv'),
    'hzrabpwezg': (10, 'asdf'),
    'vwptfsjrqz': (4, 'asdf'),
    'yusnpftjst': (5, 'qwer'),
    'cqwfbjaons': (6, 'qwer'),
    'qkbukhkbmj': (10, 'qwer'),
    'uhdmtxroej': (3, 'zxcv'),
    'otmctubpuw': (7, 'asdf'),
    'hmlsyelhog': (0, 'qwer'),
    'cgaeepubyp': (7, 'qwer'),
    'mtbxchryxw': (8, 'zxcv'),
    'gdxyclvewy': (7, 'zxcv'),
    'sjjwqjdkqi': (3, 'asdf'),
    'ydxivgkjnw': (9, 'qwer'),
    'ukivnqjrnz': (2, 'asdf'),
    'bvrjglvmkp': (6, 'zxcv'),
    'ivpxhlgjns': (4, 'asdf'),
    'tndzecmhuy': (10, 'asdf'),
    'lqqwimamry': (9, 'qwer'),
    'vuwzmplegf': (3, 'asdf'),
    'tiejokgixf': (7, 'zxcv'),
    'gqttnggxla': (2, 'zxcv'),
    'oriwcivlnn': (5, 'zxcv'),
    'ajpjzadqza': (7, 'asdf'),
    'innidxtqzu': (5, 'asdf'),
    'cvvirynjrx': (3, 'zxcv'),
    'gepiqlmojx': (0, 'zxcv'),
    'lmuiaridka': (6, 'qwer'),
    'jbtfticvhl': (9, 'zxcv'),
    'ffzaeyyusm': (10, 'zxcv'),
    'kiixohhvit': (1, 'zxcv'),
    'avhmhtppkb': (10, 'asdf'),
    'vsgdkkgxym': (0, 'qwer'),
    'qdklsfeych': (1, 'asdf'),
    'pktoigckcz': (6, 'zxcv'),
    'vmwqydgxzp': (3, 'asdf'),
    'qzsikhosvb': (6, 'qwer'),
    'rradmcazsc': (5, 'zxcv'),
    'metcsibchv': (3, 'asdf'),
    'ztiblhkats': (1, 'zxcv'),
    'iwkqgioiqj': (0, 'zxcv'),
    'bzmwquddmm': (1, 'asdf'),
    'tsjjfmgeru': (8, 'asdf'),
    'oleeqeeilq': (6, 'qwer'),
    'awvrhybvua': (3, 'asdf'),
    'wzsopzvfgu': (4, 'zxcv'),
    'vlexxzbmdq': (5, 'zxcv'),
    'mpoeecwylu': (6, 'zxcv'),
    'njafddbvjn': (10, 'zxcv'),
    'amsaaulclz': (2, 'zxcv'),
    'selfpfdstf': (9, 'zxcv'),
    'zizijsaaiu': (7, 'asdf'),
    'qndqgegeiw': (5, 'zxcv'),
    'zqkmunaugj': (9, 'qwer'),
    'lepzgwieok': (3, 'qwer'),
    'nsdmnuywzd': (5, 'zxcv'),
    'ivxkvbpgdt': (6, 'zxcv'),
    'grzfuuiebt': (7, 'asdf'),
    'oboobjduqq': (0, 'asdf'),
    'ijljpupusj': (8, 'asdf'),
    'ipfybumzzg': (0, 'zxcv'),
    'swkrndotdk': (2, 'zxcv'),
    'rkuxguantq': (8, 'asdf'),
    'jxvwlhccin': (7, 'qwer'),
    'xhqkzrzjsn': (8, 'asdf'),
    'vnefvzxlth': (8, 'zxcv'),
    'hawvlbtfcb': (2, 'asdf'),
    'dcmuxdctkk': (4, 'asdf'),
    'famqwudycs': (6, 'asdf'),
    'zctqrrllyz': (2, 'asdf'),
    'shzriihifm': (6, 'asdf'),
    'hgxdiiufyr': (7, 'asdf'),
    'oehubvnoyl': (3, 'zxcv'),
    'qaumcljsky': (0, 'zxcv'),
    'dlyzvjmyqj': (10, 'zxcv'),
    'ilkbqqcfdo': (9, 'asdf'),
    'jfilclpeey': (5, 'qwer'),
    'wclieffaqr': (9, 'zxcv'),
    'lsrwoefqip': (7, 'zxcv'),
    'bxtddcptal': (0, 'qwer'),
    'kcbocitezl': (0, 'qwer'),
    'bsyojcvcoi': (7, 'qwer'),
    'jxvfpajpoe': (9, 'zxcv'),
    'svbrekwynq': (10, 'qwer'),
    'ufyyzczfig': (5, 'zxcv'),
    'oevcurtacy': (1, 'qwer'),
    'yblnswqftq': (9, 'qwer'),
    'kitfdoqlvz': (1, 'qwer'),
    'nupsqxupqb': (1, 'qwer'),
    'pmgixqlwzb': (8, 'qwer'),
    'crfmdfodre': (1, 'qwer'),
    'bdbyibtbsy': (2, 'asdf'),
    'hsaawgoahp': (3, 'zxcv'),
    'yzmxsvrevm': (3, 'asdf'),
    'robdgyvfsc': (10, 'qwer'),
    'hqtoojtdkt': (0, 'asdf'),
    'qjfnddwqxp': (6, 'qwer'),
    'puboyzmvge': (9, 'asdf'),
    'zmipflzrxo': (5, 'zxcv'),
    'hbfmhtbqkt': (7, 'zxcv'),
    'mrgpskzgdn': (7, 'asdf'),
    'igkfbuuhzb': (6, 'asdf'),
    'nysfmkfxzs': (0, 'qwer'),
    'tgaklgegig': (4, 'zxcv'),
    'xcowutixie': (10, 'qwer'),
    'shrtasybcb': (1, 'asdf'),
    'huxmmnmcxm': (9, 'asdf'),
    'sajnnrusfa': (1, 'zxcv'),
    'jfgxicgazc': (4, 'qwer'),
    'yfiaeiavdd': (2, 'qwer'),
    'pwqziitioc': (5, 'qwer'),
    'kbsrlbrnjv': (7, 'asdf'),
    'dkkbxepjkv': (8, 'asdf'),
    'jpcyfaozme': (9, 'asdf'),
    'zafhvybrfw': (5, 'zxcv'),
    'ymuzocyxwg': (3, 'qwer'),
    'rjldjhoixo': (4, 'qwer'),
    'rovkrqzujj': (6, 'zxcv'),
    'ouqnejymbh': (3, 'zxcv'),
    'yaluwtcvbi': (2, 'zxcv'),
    'pdhfdwnjwc': (5, 'zxcv'),
    'bciqzbpxag': (2, 'zxcv'),
    'lkxbfjxnjs': (5, 'asdf'),
    'jfrmdrgbid': (0, 'asdf'),
    'mrvilbqooy': (0, 'zxcv'),
    'bxjdplimek': (5, 'asdf'),
    'mgrzrnucrl': (10, 'asdf'),
    'mvvavwwgay': (8, 'qwer'),
    'fpqffnphay': (6, 'zxcv'),
    'exlynlniuz': (2, 'zxcv'),
    'kxotmwewpd': (5, 'asdf'),
    'rbhsyvxffj': (1, 'asdf'),
    'jfepobqvob': (5, 'asdf'),
    'bysymbqate': (4, 'asdf'),
    'huwiajeoip': (0, 'asdf'),
    'dpxmnrcmkw': (3, 'asdf'),
    'zyvqucktdj': (6, 'zxcv'),
    'goxihrwicu': (8, 'asdf'),
    'meakruxygj': (2, 'asdf'),
    'ihnycosrzs': (6, 'qwer'),
    'zvkqosoobq': (1, 'zxcv'),
    'nqaxhmjwmw': (6, 'zxcv'),
    'udlqiemvwt': (6, 'zxcv'),
    'tojcutpeno': (9, 'qwer'),
    'eezlmvsfzl': (8, 'qwer'),
    'lkqetigkmh': (8, 'qwer'),
    'mzcxzmaetu': (1, 'qwer'),
    'tyesbxgdmf': (10, 'asdf'),
    'fyzcnvsxsm': (9, 'qwer'),
    'fcolkopgmx': (7, 'zxcv'),
    'egifkfampq': (1, 'qwer'),
    'hnvoauzdoq': (3, 'zxcv'),
    'spofhbbrta': (3, 'qwer'),
    'cdmkcpuhqg': (3, 'qwer'),
    'bkqfpdpgdm': (5, 'qwer'),
    'qjwlkxtvzy': (7, 'asdf'),
    'pxlnnloenc': (0, 'qwer'),
    'bznjmbneqo': (6, 'asdf'),
    'uxzqgtnxuj': (9, 'zxcv'),
    'sascrjlivt': (6, 'zxcv'),
    'bhfetmptwr': (10, 'asdf'),
    'wrnnvldwef': (9, 'asdf'),
    'yokoclfczt': (6, 'qwer'),
    'fygbtrvbtm': (4, 'asdf'),
    'angcmkufmj': (6, 'zxcv'),
    'vwromsohij': (0, 'asdf'),
    'itklvcctkq': (4, 'asdf'),
    'zqjexnbzjk': (4, 'asdf'),
    'wzgprveqzn': (10, 'zxcv'),
    'jgtoqtdxaw': (8, 'qwer'),
    'gmbwffkdks': (9, 'zxcv'),
    'rzmvmsfqbs': (2, 'qwer'),
    'cpttjzvzgv': (7, 'qwer'),
    'ljyekbehix': (0, 'zxcv'),
    'hncxgpivfv': (3, 'zxcv'),
    'lxwcbsptfe': (3, 'zxcv'),
    'jruaxfmsni': (6, 'asdf'),
    'rnxqpcanlg': (6, 'asdf'),
    'qojuquxdcf': (6, 'qwer'),
    'vklzjvoacb': (6, 'qwer'),
    'awsivryzes': (1, 'asdf'),
    'ewviyoptbe': (8, 'asdf'),
    'gbakxppmnk': (7, 'zxcv'),
    'fsntkgajks': (10, 'qwer'),
    'anssentmtn': (1, 'asdf'),
    'nhscistrtt': (2, 'qwer'),
    'snyrqfguvc': (9, 'qwer'),
    'zvqhogwjwi': (5, 'asdf'),
    'cdxkzkfbir': (4, 'qwer'),
    'dzsbybngmv': (2, 'zxcv'),
    'vxdsreryoo': (0, 'asdf'),
    'eldcujhdrw': (4, 'qwer'),
    'ezqzubyzqc': (3, 'zxcv'),
    'zargjosulw': (3, 'zxcv'),
    'kkeletduaf': (6, 'zxcv'),
    'anfegoyonc': (5, 'qwer'),
    'aaqjghewtc': (5, 'asdf'),
    'bgriatoklg': (4, 'qwer'),
    'ilgdwfbwfd': (5, 'asdf'),
    'zwnkznwtmw': (7, 'zxcv'),
    'frrgehwyxa': (4, 'zxcv'),
    'anwtlymixg': (8, 'zxcv'),
    'umyldyadrw': (10, 'zxcv'),
    'lwvkrizhae': (9, 'qwer'),
    'rfwhhtxutv': (8, 'asdf'),
    'ikwccobtdh': (0, 'qwer'),
    'ulqtmykfxd': (4, 'asdf'),
    'nbamsoexri': (1, 'qwer'),
    'ilgchfcixc': (8, 'asdf'),
    'gtylqpfdvv': (7, 'zxcv'),
    'txxcyqrhoi': (9, 'zxcv'),
    'wveardvsij': (4, 'asdf'),
    'ygiamvfusl': (5, 'qwer'),
    'pzjbcvcotp': (2, 'asdf'),
    'ivlytxmzwu': (6, 'zxcv'),
    'tyahcitstz': (3, 'asdf'),
    'bxikjqaxgo': (6, 'zxcv'),
    'nogxgiwsqs': (7, 'asdf'),
    'yftxptdvdt': (9, 'asdf'),
    'enyajhicqt': (0, 'asdf'),
    'ufdroccvvq': (4, 'asdf'),
    'aokrayvrhb': (2, 'qwer'),
    'nspqegsvgf': (10, 'zxcv'),
    'ikadgvqzab': (7, 'zxcv'),
    'ikftmydskr': (7, 'zxcv'),
    'ttiecywqtt': (6, 'zxcv'),
    'uvhdvyhfwt': (9, 'qwer'),
    'ljffhywxov': (10, 'zxcv'),
    'cvftcnuayw': (9, 'asdf'),
    'csiluitxmn': (6, 'asdf'),
    'ogwuogidkh': (0, 'qwer'),
    'dguuainpzu': (7, 'qwer'),
    'boybkxzrag': (2, 'qwer'),
    'oxrkgwenhj': (4, 'qwer'),
    'qrbttxiwmq': (7, 'asdf'),
    'yrpyoyhzoe': (8, 'asdf'),
    'ovuaobeodt': (6, 'zxcv'),
    'cyubjryyei': (7, 'qwer'),
    'sqglvtlpno': (6, 'asdf'),
    'yaufuuvkim': (7, 'zxcv')
}

df = pd.DataFrame(my_dictionary.items(), columns=['column1', 'temp'])
df['column2'] = df['temp'].apply(lambda x: random.randint(0, 10))
df['column3'] = df['temp'].apply(lambda x: random.choice(['asdf', 'qwer', 'zxcv']))
df = df[['column1', 'column2', 'column3']]

if __name__ == '__main__':
    dict_finder(my_dictionary, 'crfmdfodre')
    df_finder(df, 'crfmdfodre')




event = {
    "event": "init__deviceId",
    "client_event_time": "2023-07-14T00:00:00+00:00",
    "event_properties": {
        "device_id": "d6294066-716b-4b78-b1ba-28dee10aeb74"
    },
    "context": {
        "_server": {
            "x-forwarded-for": "10.10.2.57",
            "x-forwarded-proto": "https",
            "x-forwarded-port": "443",
            "host": "data-nw-weaver.wanted.co.kr",
            "x-amzn-trace-id": "Root=1-64b0e2bc-4e0b96b23b0e99647a41ae3f",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "accept": "*/*",
            "sec-fetch-site": "none",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "cookie": "_gcl_au=1.1.1535026358.1686102371; _fbp=fb.2.1686102371572.843716002; amp_c29b58=eFk3kS0lyZ9ULPiP11JFU6...1h2pqq488.1h2psd6s3.0.0.0; WWW_ONEID_ACCESS_TOKEN=7641d615ed0245679b14984907782bfd; WWWTEST_ONEID_ACCESS_TOKEN=34bf8e54b078451b97542b3dabaca418; DEV_ONEID_ACCESS_TOKEN=28d3af174b3d4eb89baf2a5410f5acec; AMP_MKTG_fde632d3af=JTdCJTdE; _gaexp=GAX1.3.NXIspvdNRi68ByYqGiWLKg.19614.0; _gac_UA-62498866-1=1.1687159738.CjwKCAjw-b-kBhB-EiwA4fvKrEbsPZf9CWSsJreujJ45ZGW82o79Z5iUV0MpWUSfp9ec5PjghGG1TBoC-e4QAvD_BwE; ch-veil-id=ba69e5c9-f8c1-4e5e-aaa5-e7f818eb579a; _gcl_aw=GCL.1687227710.CjwKCAjw-b-kBhB-EiwA4fvKrEbsPZf9CWSsJreujJ45ZGW82o79Z5iUV0MpWUSfp9ec5PjghGG1TBoC-e4QAvD_BwE; _vwo_uuid_v2=D63B885C0A9C4FC076D8C61D2D1FF3B05|822dfd7b55d44e6d391ca8818545c3f4; _ga_VNXZFPCDCX=GS1.3.1687765732.2.0.1687765732.0.0.0; amp_15af52=Thw72pcDC3VlxLao85a9Ps...1h3tsunad.1h3tt9nnc.c.3.f; amp_d08dcd=VDyvHdj3A9EN-Fka5E9wAJ.MjM3NTg1NA==..1h4r8sp0s.1h4r8spl5.14.16.2a; _ga_4XX1N5VVJ2=GS1.1.1688951133.14.0.1688951133.0.0.0; amp_d16863=vUUgtakStZwlKudQVATPHK.MTA1MDQ3..1h4ula589.1h4ula5uj.53.s.5v; _ga_Y4BDQ5FKZ0=GS1.1.1688969660.20.0.1688969660.60.0.0; weaver-device-id=d6294066-716b-4b78-b1ba-28dee10aeb74; _ga_JMVHE9R721=GS1.1.1689069037.16.0.1689069041.0.0.0; _ga_YKFMYZ2YXR=GS1.1.1689069037.15.0.1689069041.0.0.0; _ga=GA1.1.445278865.1686102371; ab.storage.sessionId.a1ad2869-0a99-4248-bd1d-069f830ccc4e=%7B%22g%22%3A%229e81922e-0ad1-a882-4a45-07bcdcc40138%22%2C%22e%22%3A1689095906792%2C%22c%22%3A1689094106792%2C%22l%22%3A1689094106792%7D; ab.storage.deviceId.a1ad2869-0a99-4248-bd1d-069f830ccc4e=%7B%22g%22%3A%226c3126d0-d044-0711-5ab5-a9cd9e123229%22%2C%22c%22%3A1680884594885%2C%22l%22%3A1689094106792%7D; ab.storage.userId.a1ad2869-0a99-4248-bd1d-069f830ccc4e=%7B%22g%22%3A%22671476%22%2C%22c%22%3A1689094106792%2C%22l%22%3A1689094106793%7D; amp_00a215=9FXT679zVmEpx8C8WG1Viw...1h52tlbqj.1h52tlbqk.f.d.s; amp_edddb6=h--9fNRFWngg13cepxEzVh.Njgx..1h59fba1k.1h59fbb1m.4f.10.5f; AMP_fde632d3af=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI3OGVkZjdiZi01ZmJjLTQ4MmEtOTM1Ny0xZmQxZGIxMzQ4MjQlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNjg3MTUyMzg1OTgzJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRJZCUyMiUzQTAlN0Q=; _ga_GF6EWWFSES=GS1.1.1689313978.14.1.1689313979.0.0.0"
        }
    }
}

event2 = {
    "event": "position__list__view",
    "client_event_time": "2023-05-25T15:07:42+00:00",
    "user_id": "444451",
    "event_properties": {
        "jobCategoryId": "518",
        "jobCategory": "IT",
        "jobRoleId": "all",
        "jobRole": "all"
    },
    "user_properties": {
        "one_id": "VYoLMEZJJ9FoTBGb5JhnhZ"
    },
    "context": {
        "service": "wanted",
        "_server": {
            "x-forwarded-for": "192.168.20.197",
            "x-forwarded-proto": "https",
            "x-forwarded-port": "443",
            "host": "data-nw-weaver.wantedlab.com",
            "x-amzn-trace-id": "Root=1-64b5e737-2f3317c61820771332461b2c",
            "content-length": "345",
            "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
            "accept": "application/json",
            "content-type": "application/json",
            "sec-ch-ua-mobile": "?0",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "sec-ch-ua-platform": "\"macOS\"",
            "origin": "https://data-nw-weaver.wantedlab.com",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://data-nw-weaver.wantedlab.com/docs",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "cookie": "weaver-device-id=413e0bc0-99e8-4ce6-8914-89e6afd16f18"
        }
    }
}


if __name__ == '__main__':
    context = event.pop('context')
    context2 = event2.pop('context')

    oce = OrdinaryClassEvent(event, context)
    oc2 = OrdinaryClassEvent(event2, context2)