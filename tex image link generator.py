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
S = st.text_area(label='Input tex equations',
                 value=S_default_value,
                 height=text_area_height)

# display styleを個々に追加したい
style_dict = {'default': '\displaystyle ',
              'inline': '\\textstyle '}
style_prefix = style_dict[
    st.selectbox('Select style', list(style_dict.keys()))]

size_dict = {'M': '',
             'L': '\large ',
             '2L': '\Large ',
             '3L': '\LARGE ',
             '4L': '\huge ',
             '5L': '\Huge '}

size_prefix = size_dict[st.selectbox('Select size', list(size_dict.keys()))]


# encode
S_quote = parse.quote_plus(size_prefix + style_prefix + S)

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

'## HTML'
st.code(TAG, language='html')

'## Markdown'
st.code(MD, language='')
# st.code(URL)


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
