import streamlit as st
import urllib.parse as parse


# fixed values
S_default_value = r'''\begin{align*}
R(g) &= \frac{1}{n} \sum_{i=1}^{n} \ell(y_i,g(x_i))\\
&=\frac{1}{2n} (\mathbf{X}\boldsymbol{w}-\mathbf{y})^T (\mathbf{X}\boldsymbol{w}-\mathbf{y})
\end{align*}
'''
T_default_value = parse.quote_plus(S_default_value)
text_area_height = 220

# input
st.title('tex image link generator')
S = st.text_area(label='input tex commands',
                 value=S_default_value,
                 height=text_area_height)
size_list = ['M', 'L', '2L', '3L', '4L', '5L']
size = st.selectbox('size?', size_list)

size_prefix = ['', '\large ', '\Large ', '\LARGE ',
               '\huge ', '\Huge '][size_list.index(size)]


# encode
S_quote = parse.quote_plus(size_prefix + S)

url_prefix = 'https://render.githubusercontent.com/render/math?math='
URL = url_prefix + S_quote

tag_prefix = '<img src="'
tag_suffix = '">'
TAG = tag_prefix + URL + tag_suffix

md_prefix = '![]('
md_suffix = ')'

MD = md_prefix + URL + md_suffix

'preview'

st.markdown(TAG, unsafe_allow_html=True)
''
''

'result'

# st.code(URL)
st.code(TAG, language='html')
st.code(MD, language='')


# 'メモ書き'
# 'latex result'
# st.latex(S)
# 'markdown tex result'
# st.markdown('$$' + S + '$$')


st.title('tex image link decoder')
# input
T = st.text_area(label='https://render.githubusercontent.com/render/math?math=',
                 value=T_default_value,
                 height=text_area_height)


# decode
'result'
T_unquote = parse.unquote_plus(T)
st.code(T_unquote, language='')
