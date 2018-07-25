# -*- coding:utf-8 -*- 

from .germancredit import germancredit
from .splitdf import split_df
from .info_value import iv
from .var_filter import var_filter
from .woebin import (woebin, woebin_ply, woebin_plot, woebin_adj)
from .perf import (perf_eva, perf_psi)
from .scorecard import (scorecard, scorecard_ply)
from .options import (set_options, get_options)
set_options(colors=('yellow','blue'))
set_options(outcomes=('God','Bad'))


