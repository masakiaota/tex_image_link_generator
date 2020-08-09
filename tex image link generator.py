import streamlit as st
import urllib.parse as parse


# fixed values
S_default_value = r'''\begin{align*}
R(g) &= \frac{1}{n} \sum_{i=1}^{n} \ell(y_i,g(x_i))\\
&=\frac{1}{2n} (\mathbf{X}\boldsymbol{w}-\mathbf{y})^T (\mathbf{X}\boldsymbol{w}-\mathbf{y})
\end{align*}
'''

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

tag_prefix = '<img src=\n"'
tag_suffix = '" \nalt="' + S + '">'
TAG = tag_prefix + URL + tag_suffix

md_prefix = '![' + S + ']('
md_suffix = ')'

MD = md_prefix + URL + md_suffix

'## Image Preview'

st.markdown(TAG, unsafe_allow_html=True)


# st.code(URL)
'## HTML'
st.code(TAG, language='html')
'## Markdown'
st.code(MD, language='')


# 'メモ書き'
# 'latex result'
# st.latex(S)
# 'markdown tex result'
# st.markdown('$$' + S + '$$')


# reference
''
''
''
'Project repository https://github.com/masakiaota/tex_image_link_generator'
