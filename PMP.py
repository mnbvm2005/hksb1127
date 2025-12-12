import streamlit as st
from datetime import datetime, timedelta
import uuid
import pandas as pd
from io import BytesIO
from collections import defaultdict
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.express as px
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from openpyxl import Workbook
from pandas import ExcelWriter
import sys
import subprocess
import os
import deepseek
# 页面配置
st.set_page_config(
    page_title="PMP系统",
    page_icon="📋",
    layout="wide"
)


# 修复rerun方法兼容问题
def rerun():
    """兼容新旧版本Streamlit的页面刷新方法"""
    if hasattr(st, 'experimental_rerun'):
        st.experimental_rerun()
    else:
        st.rerun()


import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

# 页面配置
st.set_page_config(
    page_title="PMP系统 - 登录",
    page_icon="📋",
    layout="centered"
)


# 修复rerun方法兼容问题
def rerun():
    """兼容新旧版本Streamlit的页面刷新方法"""
    if hasattr(st, 'experimental_rerun'):
        st.experimental_rerun()
    else:
        st.rerun()


import streamlit as st

# 页面配置
st.set_page_config(
    page_title="PMP系统 - 登录",
    page_icon="📋",
    layout="wide"
)


# 修复rerun方法兼容问题
def rerun():
    """兼容新旧版本Streamlit的页面刷新方法"""
    if hasattr(st, 'experimental_rerun'):
        st.experimental_rerun()
    else:
        st.rerun()


import streamlit as st

# 页面配置
st.set_page_config(
    page_title="PMP系统 - 登录",
    page_icon="📋",
    layout="wide"
)


# 修复rerun方法兼容问题
def rerun():
    """兼容新旧版本Streamlit的页面刷新方法"""
    if hasattr(st, 'experimental_rerun'):
        st.experimental_rerun()
    else:
        st.rerun()


import streamlit as st

# 页面配置
st.set_page_config(
    page_title="PMP系统 - 登录",
    page_icon="📋",
    layout="wide"
)


# 修复rerun方法兼容问题
def rerun():
    """兼容新旧版本Streamlit的页面刷新方法"""
    if hasattr(st, 'experimental_rerun'):
        st.experimental_rerun()
    else:
        st.rerun()


import streamlit as st

# 页面配置
st.set_page_config(
    page_title="PMP系统 - 登录",
    page_icon="📋",
    layout="wide"
)


# 修复rerun方法兼容问题
def rerun():
    """兼容新旧版本Streamlit的页面刷新方法"""
    if hasattr(st, 'experimental_rerun'):
        st.experimental_rerun()
    else:
        st.rerun()


# ------------------------------
# 登录界面美化（专业版）
# ------------------------------
# 初始化登录状态
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_type' not in st.session_state:
    st.session_state.user_type = None

# 登录界面
if not st.session_state.logged_in:
    # 专业商务风背景（深蓝色科技网格，无多余元素）
    page_bg_img = """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1551434678-e076c223a692?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-color: #1a202c; /*  fallback 背景色 */
    }

    .login-container {
        background-color: rgba(255, 255, 255, 0.95); /* 提高不透明度，增强可读性 */
        padding: 2.5rem 3rem;
        border-radius: 12px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        max-width: 420px;
        margin: 6rem auto;
    }

    .title {
        color: #1e293b; /* 深灰蓝色，专业稳重 */
        text-align: center;
        margin-bottom: 1rem;
        font-size: 1.8rem;
        font-weight: 700;
        text-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }

    .subtitle {
        color: #475569; /* 中灰色，不刺眼 */
        text-align: center;
        margin-bottom: 2rem;
        font-size: 1rem;
        font-weight: 500;
    }

    .stRadio > div {
        display: flex;
        justify-content: center;
        gap: 2.5rem;
        margin-bottom: 1.8rem;
    }

    .stRadio label {
        color: #334155; /* 单选框文字加深，清晰可见 */
        font-weight: 500;
    }

    .stButton > button {
        width: 100%;
        background-color: #2563eb; /* 专业商务蓝，不浮夸 */
        color: white;
        font-size: 1.05rem;
        padding: 0.9rem;
        border-radius: 8px;
        border: none;
        transition: all 0.3s ease;
        font-weight: 500;
    }

    .stButton > button:hover {
        background-color: #1d4ed8; /* hover加深，有质感 */
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(37, 99, 235, 0.3);
    }

    .stTextInput > div > input {
        border-radius: 8px;
        padding: 0.9rem;
        border: 1px solid #e2e8f0;
        font-size: 1rem;
        color: #1e293b; /* 输入文字颜色加深 */
    }

    .stTextInput > div > input::placeholder {
        color: #94a3b8; /* 占位符灰色，不突兀 */
    }

    .error-message {
        color: #dc2626; /* 错误提示红色，醒目但不刺眼 */
        text-align: center;
        margin-top: 1rem;
        font-size: 0.95rem;
        font-weight: 500;
    }

    .success-message {
        color: #059669; /* 成功提示绿色，稳重 */
        text-align: center;
        margin-top: 1rem;
        font-size: 0.95rem;
        font-weight: 500;
    }
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)

    # 登录容器
    with st.container():
        st.markdown('<div class="login-container">', unsafe_allow_html=True)

        # 系统标题+副标题
        st.markdown('<h1 class="title">📋 PMP项目管理系统</h1>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">专业项目管理 · 高效协同办公</p>', unsafe_allow_html=True)

        # 登录类型选择
        login_type = st.radio("选择登录身份", ["管理员登录", "普通用户登录"], horizontal=True)

        # 垂直间距
        st.write("&nbsp;")

        # 账号密码输入框
        username = st.text_input("账号", placeholder="请输入登录账号")
        password = st.text_input("密码", type="password", placeholder="请输入登录密码")

        # 垂直间距
        st.write("&nbsp;")

        # 登录按钮+验证逻辑
        if st.button("安全登录"):
            if login_type == "管理员登录":
                if username == "1" and password == "1":
                    st.session_state.logged_in = True
                    st.session_state.user_type = "admin"
                    st.markdown('<p class="success-message">✅ 管理员登录成功，正在跳转...</p>', unsafe_allow_html=True)
                    rerun()
                else:
                    st.markdown('<p class="error-message">❌ 账号或密码错误（初始账号密码均为1）</p>',
                                unsafe_allow_html=True)
            elif login_type == "普通用户登录":
                if username == "2" and password == "2":
                    st.session_state.logged_in = True
                    st.session_state.user_type = "user"
                    st.markdown('<p class="success-message">✅ 用户登录成功，正在跳转...</p>', unsafe_allow_html=True)
                    rerun()
                else:
                    st.markdown('<p class="error-message">❌ 账号或密码错误（初始账号密码均为2）</p>',
                                unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # 阻止后续代码执行
    st.stop()
# 这里是你原来的系统主界面代码
st.write(f"欢迎回来，{st.session_state.user_type}用户！")
# ...
# ------------------------------
# 初始化数据（会话状态存储）  ← 原有数据初始化放在登录代码之后
# ------------------------------
if 'departments' not in st.session_state:
    st.session_state.departments = {}
# 其他数据初始化...
# 页面配置
st.set_page_config(
    page_title="PMP系统",
    page_icon="📋",
    layout="wide"
)


# 修复rerun方法兼容问题
def rerun():
    """兼容新旧版本Streamlit的页面刷新方法"""
    if hasattr(st, 'experimental_rerun'):
        st.experimental_rerun()
    else:
        st.rerun()


# ------------------------------
# 初始化数据（会话状态存储）
# ------------------------------
# 原有组织管理数据
if 'departments' not in st.session_state:
    st.session_state.departments = {}

if 'positions' not in st.session_state:
    st.session_state.positions = {}

if 'employees' not in st.session_state:
    st.session_state.employees = {}

if 'custom_position_types' not in st.session_state:
    st.session_state.custom_position_types = []

if 'search_keyword' not in st.session_state:
    st.session_state.search_keyword = ""

# 项目管理相关数据
if 'projects' not in st.session_state:
    st.session_state.projects = {}

if 'pbs_data' not in st.session_state:
    st.session_state.pbs_data = {}  # PBS数据：{pbs_id: {项目ID、父级ID、名称、编号等}}

if 'wbs_data' not in st.session_state:
    st.session_state.wbs_data = {}  # WBS数据：{wbs_id: {关联PBS、父级ID、名称、编号等}}

# 新增CS和BS相关数据结构
if 'cs_plans' not in st.session_state:
    st.session_state.cs_plans = {}  # 存储CS计划：{cs_id: {任务ID、依赖关系、工期等}}
if 'cs_tasks' not in st.session_state:
    st.session_state.cs_tasks = {}  # 存储CS任务：{task_id: {名称、工期、依赖、开始/结束时间等}}
if 'dependency_types' not in st.session_state:
    st.session_state.dependency_types = ["FS（完成→开始）", "SS（开始→开始）", "FF（完成→完成）", "SF（开始→完成）"]

if 'bs_metrics' not in st.session_state:
    st.session_state.bs_metrics = {}  # 存储BS指标：{metric_id: {维度、目标、实际、责任人等}}

# 其他预留数据结构保持不变
if 'bs_plans' not in st.session_state:
    st.session_state.bs_plans = {}
if 'approval_records' not in st.session_state:
    st.session_state.approval_records = []
if 'contract_records' not in st.session_state:
    st.session_state.contract_records = []
if 'plan_recovery' not in st.session_state:
    st.session_state.plan_recovery = []
if 'recovery_records' not in st.session_state:
    st.session_state.recovery_records = []
if 'overall_plans' not in st.session_state:
    st.session_state.overall_plans = {}
if 'progress_detection' not in st.session_state:
    st.session_state.progress_detection = []
if 'progress_monitoring' not in st.session_state:
    st.session_state.progress_monitoring = {}


# ------------------------------
# 工具函数
# ------------------------------
def generate_unique_id(prefix=""):
    return f"{prefix}-{str(uuid.uuid4())[:8]}"


def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")


def get_employee_name(emp_id):
    return st.session_state.employees.get(emp_id, {}).get("name", "未知人员")


def get_employee_id(name):
    for emp_id, emp in st.session_state.employees.items():
        if emp["name"] == name:
            return emp_id
    return None


def get_dept_name(dept_id):
    return st.session_state.departments.get(dept_id, {}).get("name", "未知部门")


def get_dept_members(dept_id):
    if not dept_id or dept_id not in st.session_state.departments:
        return []
    return [(emp_id, get_employee_name(emp_id))
            for emp_id in st.session_state.departments[dept_id].get("members", [])]


def judge_org_form():
    project_managers = 0
    functional_managers = 0
    cross_dept_employees = 0

    for pos in st.session_state.positions.values():
        pos_type = pos["type"]
        if pos_type in ["项目经理", "项目经理主管"]:
            project_managers += len(pos["employees"])
        elif pos_type == "职能主管":
            functional_managers += len(pos["employees"])

    for emp in st.session_state.employees.values():
        if len(emp.get("dept_ids", [])) >= 2:
            cross_dept_employees += 1

    if project_managers > functional_managers and cross_dept_employees > 0:
        return "强矩阵"
    elif functional_managers > project_managers and cross_dept_employees == 0:
        return "弱矩阵"
    elif project_managers == functional_managers and cross_dept_employees > 0:
        return "平衡式"
    elif cross_dept_employees > 0 and project_managers > 0 and functional_managers > 0:
        return "复合式"
    else:
        return "未明确（请配置岗位和人员）"


def get_org_form_desc(form_type):
    desc = {
        "强矩阵": {"优势": "项目经理权限高，决策效率高", "劣势": "部门协作成本高，资源冲突风险大",
                   "适用": "大型复杂项目、创新型项目"},
        "弱矩阵": {"优势": "部门管理为主，资源利用率高", "劣势": "项目经理权限低，跨部门协调困难",
                   "适用": "小型项目、常规性工作"},
        "平衡式": {"优势": "权限平衡，兼顾部门与项目需求", "劣势": "决策效率低，易出现责任不清",
                   "适用": "中等规模项目、跨部门协作项目"},
        "复合式": {"优势": "灵活应对复杂场景，多项目并行管理", "劣势": "管理复杂，需要高级协调能力",
                   "适用": "多项目集群、企业级转型项目"},
        # 补充对未明确类型的描述（原代码此处键错误，写成了"未明确..."）
        "未明确（请配置岗位和人员）": {"优势": "-", "劣势": "-", "适用": "请先完善岗位和人员配置"}
    }
    return desc[form_type]


def generate_org_chart():
    if not st.session_state.departments:
        return None

    dept_children = {dept_id: [] for dept_id in st.session_state.departments.keys()}
    root_depts = []

    for dept_id, dept in st.session_state.departments.items():
        parent_id = dept.get("parent_dept_id")
        if parent_id and parent_id in dept_children:
            dept_children[parent_id].append(dept_id)
        else:
            root_depts.append(dept_id)

    def add_nodes(dept_id, parent):
        dept = st.session_state.departments[dept_id]
        label = f"{dept['name']}\n({dept['manager'] or '无负责人'})"
        children = dept_children.get(dept_id, [])
        node = {"id": dept_id, "label": label, "parent": parent, "children": []}
        for child_id in children:
            node["children"].append(add_nodes(child_id, dept_id))
        return node

    tree_data = [add_nodes(dept_id, "") for dept_id in root_depts]
    fig = go.Figure(go.Treemap(
        ids=[node["id"] for node in tree_data],
        labels=[node["label"] for node in tree_data],
        parents=[node["parent"] for node in tree_data],
        branchvalues="total"
    ))
    fig.update_layout(title="组织架构图", margin=dict(t=50, l=25, r=25, b=25))
    return fig


def export_to_excel():
    dept_data = []
    for dept in st.session_state.departments.values():
        dept_data.append({
            "部门ID": dept["id"], "部门名称": dept["name"], "层级": dept["level"],
            "上级部门": dept["parent_dept"], "负责人": dept["manager"], "状态": dept["status"]
        })

    emp_data = []
    for emp in st.session_state.employees.values():
        emp_data.append({
            "人员ID": emp["id"], "姓名": emp["name"], "联系方式": emp["contact"],
            "职称": emp["title"], "所属部门": ",".join(emp["dept_names"]), "状态": emp["status"]
        })

    pos_data = []
    for pos in st.session_state.positions.values():
        pos_data.append({
            "岗位ID": pos["id"], "类型": pos["type"], "岗位名称": pos.get("name", "-"),
            "所属部门": pos["dept_name"], "主责人员": pos["manager"],
            "岗位人员": ",".join(pos["employees_names"]), "状态": pos["status"]
        })

    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        pd.DataFrame(dept_data).to_excel(writer, sheet_name="部门", index=False)
        pd.DataFrame(emp_data).to_excel(writer, sheet_name="人员", index=False)
        pd.DataFrame(pos_data).to_excel(writer, sheet_name="岗位", index=False)
    return output.getvalue()


# ------------------------------
# PBS专用工具函数
# ------------------------------
def get_pbs_children(pbs_id):
    """获取指定PBS节点的所有子节点"""
    return [pbs for pbs in st.session_state.pbs_data.values() if pbs["parent_id"] == pbs_id]


def get_pbs_parent(pbs_id):
    """获取指定PBS节点的父节点"""
    pbs = st.session_state.pbs_data.get(pbs_id)
    if not pbs or not pbs["parent_id"]:
        return None
    return st.session_state.pbs_data.get(pbs["parent_id"])


def build_pbs_hierarchy(project_id):
    """构建指定项目的PBS层级结构（树形）"""
    project_pbs = [pbs for pbs in st.session_state.pbs_data.values() if pbs["project_id"] == project_id]
    if not project_pbs:
        return []

    pbs_map = {pbs["id"]: pbs for pbs in project_pbs}
    children_map = defaultdict(list)
    root_nodes = []

    for pbs in project_pbs:
        if not pbs["parent_id"]:  # 根节点（一级计划）
            root_nodes.append(pbs)
        else:
            children_map[pbs["parent_id"]].append(pbs)

    def add_children(node):
        node_copy = node.copy()
        node_copy["children"] = [add_children(child) for child in children_map.get(node["id"], [])]
        return node_copy

    return [add_children(root) for root in root_nodes]


def calculate_pbs_作业数(pbs_id):
    """计算指定PBS节点的作业数（子节点总数）"""
    children = get_pbs_children(pbs_id)
    count = len(children)
    for child in children:
        count += calculate_pbs_作业数(child["id"])
    return count


def refresh_pbs_作业数():
    """刷新所有PBS节点的作业数"""
    for pbs_id in st.session_state.pbs_data:
        st.session_state.pbs_data[pbs_id]["作业数"] = calculate_pbs_作业数(pbs_id)


# ------------------------------
# WBS专用工具函数
# ------------------------------
def get_wbs_children(wbs_id):
    """获取指定WBS节点的所有子节点"""
    return [wbs for wbs in st.session_state.wbs_data.values() if wbs["parent_id"] == wbs_id]


def get_wbs_parent(wbs_id):
    """获取指定WBS节点的父节点"""
    wbs = st.session_state.wbs_data.get(wbs_id)
    if not wbs or not wbs["parent_id"]:
        return None
    return st.session_state.wbs_data.get(wbs["parent_id"])


def get_pbs_wbs_list(pbs_id):
    """获取指定PBS关联的所有WBS节点"""
    return [wbs for wbs in st.session_state.wbs_data.values() if wbs["pbs_id"] == pbs_id]


def generate_wbs_code(parent_id=None, pbs_id=None):
    """
    生成WBS结构化编号
    - 一级WBS（直接关联PBS）：PBS编号 + .A/B/C...
    - 二级WBS（子节点）：父级编号 + .1/2/3...
    """
    if parent_id:
        # 子节点：在父级编号后加数字
        parent_wbs = st.session_state.wbs_data.get(parent_id)
        if not parent_wbs:
            return "ERROR"

        parent_code = parent_wbs["code"]
        children = get_wbs_children(parent_id)
        # 查找最大数字后缀
        max_num = 0
        for child in children:
            suffix = child["code"].split(".")[-1]
            if suffix.isdigit():
                max_num = max(max_num, int(suffix))
        return f"{parent_code}.{max_num + 1}"

    elif pbs_id:
        # 一级节点：在PBS编号后加字母
        pbs = st.session_state.pbs_data.get(pbs_id)
        if not pbs:
            return "ERROR"

        pbs_code = pbs["code"]
        siblings = get_pbs_wbs_list(pbs_id)
        # 查找最大字母后缀（A=0, B=1...）
        max_letter_idx = -1
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for wbs in siblings:
            suffix = wbs["code"].split(".")[-1]
            if len(suffix) == 1 and suffix in letters:
                max_letter_idx = max(max_letter_idx, letters.index(suffix))
        return f"{pbs_code}.{letters[max_letter_idx + 1]}"

    return "ERROR"


def calculate_wbs_任务数(wbs_id):
    """计算指定WBS节点的子任务数"""
    children = get_wbs_children(wbs_id)
    count = len(children)
    for child in children:
        count += calculate_wbs_任务数(child["id"])
    return count


def refresh_wbs_任务数():
    """刷新所有WBS节点的任务数"""
    for wbs_id in st.session_state.wbs_data:
        st.session_state.wbs_data[wbs_id]["任务数"] = calculate_wbs_任务数(wbs_id)


# ------------------------------
# CS关键路径法工具函数
# ------------------------------
def calculate_critical_path(tasks):
    """计算关键路径、浮动时间、总工期"""
    # 初始化最早开始（ES）、最早完成（EF）、最晚开始（LS）、最晚完成（LF）
    for task_id, task in tasks.items():
        task["ES"] = 0
        task["EF"] = task["duration"]
        task["LS"] = 0
        task["LF"] = task["duration"]
        task["float"] = 0

    # 正向计算ES、EF
    for task_id, task in sorted(tasks.items(), key=lambda x: x[1].get("sequence", 0)):
        for dep in task.get("dependencies", []):
            dep_task = tasks.get(dep["task_id"])
            if dep_task:
                dep_type = dep["type"]
                if dep_type == "FS（完成→开始）":
                    es = dep_task["EF"]
                elif dep_type == "SS（开始→开始）":
                    es = dep_task["ES"]
                elif dep_type == "FF（完成→完成）":
                    es = dep_task["EF"] - task["duration"]
                elif dep_type == "SF（开始→完成）":
                    es = dep_task["ES"] - task["duration"]
                es = max(es, task["ES"])
                task["ES"] = es
                task["EF"] = es + task["duration"]

    # 反向计算LS、LF、浮动时间
    total_duration = max(task["EF"] for task in tasks.values()) if tasks else 0
    for task_id, task in sorted(tasks.items(), key=lambda x: x[1].get("sequence", 0), reverse=True):
        task["LF"] = total_duration
        task["LS"] = task["LF"] - task["duration"]
        for dep in task.get("dependencies", []):
            dep_task = tasks.get(dep["task_id"])
            if dep_task:
                dep_type = dep["type"]
                if dep_type == "FS（完成→开始）":
                    lf = dep_task["LS"]
                elif dep_type == "SS（开始→开始）":
                    lf = dep_task["LS"] + task["duration"]
                elif dep_type == "FF（完成→完成）":
                    lf = dep_task["LF"]
                elif dep_type == "SF（开始→完成）":
                    lf = dep_task["LF"] + task["duration"]
                lf = min(lf, dep_task["LF"])
                dep_task["LF"] = lf
                dep_task["LS"] = lf - dep_task["duration"]
                dep_task["float"] = dep_task["LS"] - dep_task["ES"]

    # 标记关键任务（浮动时间为0）
    for task in tasks.values():
        task["is_critical"] = task["float"] == 0

    return total_duration, tasks


def generate_gantt_chart(tasks, title="CS关键路径栈道图"):
    """生成栈道图（甘特图）"""
    df = []
    for task_id, task in tasks.items():
        start_date = datetime(2025, 1, 1) + timedelta(days=task["ES"])
        end_date = datetime(2025, 1, 1) + timedelta(days=task["EF"])
        df.append({
            "Task": task["name"],
            "Start": start_date,
            "Finish": end_date,
            "Duration": task["duration"],
            "Critical": "关键任务" if task["is_critical"] else "非关键任务"
        })

    # 定义颜色：关键任务红色，非关键任务蓝色
    colors = {"关键任务": "#FF4B4B", "非关键任务": "#1E88E5"}
    fig = ff.create_gantt(
        df,
        colors=colors,
        index_col="Critical",
        show_colorbar=True,
        title=title,
        bar_width=0.4,
        showgrid_x=True,
        showgrid_y=True
    )
    fig.update_layout(xaxis_title="时间", yaxis_title="任务", height=600)
    return fig


# ------------------------------
# BS平衡计分卡工具函数
# ------------------------------
def calculate_bs_score(metrics):
    """计算平衡计分卡各维度得分及综合得分"""
    dimensions = {
        "财务": [],
        "客户": [],
        "内部流程": [],
        "学习与成长": []
    }
    for metric in metrics.values():
        dimensions[metric["dimension"]].append(metric)

    scores = {}
    for dim, items in dimensions.items():
        total = 0
        for item in items:
            total += (item["actual"] / item["target"]) * 100 if item["target"] != 0 else 0
        scores[dim] = total / len(items) if items else 0

    scores["综合得分"] = sum(scores.values()) / len(scores) if scores else 0
    return scores


# ------------------------------
# 全局搜索功能
# ------------------------------
def global_search():
    st.sidebar.text_input(
        "全局搜索（部门/人员/岗位/项目）",
        value=st.session_state.search_keyword,
        key="search_input",
        on_change=lambda: setattr(st.session_state, "search_keyword", st.session_state.search_input)
    )

    keyword = st.session_state.search_keyword.strip().lower()
    if not keyword:
        return None

    results = {"部门": [], "人员": [], "岗位": [], "项目": []}

    for dept in st.session_state.departments.values():
        if keyword in dept["name"].lower() or keyword in dept["description"].lower():
            results["部门"].append(dept)

    for emp in st.session_state.employees.values():
        if keyword in emp["name"].lower() or keyword in emp["contact"].lower():
            results["人员"].append(emp)

    for pos in st.session_state.positions.values():
        pos_name = pos.get("name", pos["type"])
        if keyword in pos_name.lower() or keyword in pos["type"].lower():
            results["岗位"].append(pos)

    for proj in st.session_state.projects.values():
        if keyword in proj["name"].lower() or keyword in proj.get("description", "").lower():
            results["项目"].append(proj)

    return results


# ------------------------------
# 页面导航
# ------------------------------
st.title("📋 PMP项目管理系统")

# 全局搜索结果展示
search_results = global_search()
if search_results and any(results for results in search_results.values()):
    with st.expander(f"搜索结果：「{st.session_state.search_keyword}」", expanded=True):
        for category, items in search_results.items():
            if items:
                st.subheader(f"{category}")
                for item in items:
                    if category == "部门":
                        st.write(f"- {item['name']}（{item['level']}）")
                        if st.button("查看", key=f"search_dept_{item['id']}"):
                            st.session_state.active_tab = "部门管理"
                            st.session_state.selected_dept_id = item["id"]
                            rerun()
                    elif category == "人员":
                        st.write(f"- {item['name']}（{','.join(item['dept_names'])}）")
                        if st.button("查看", key=f"search_emp_{item['id']}"):
                            st.session_state.active_tab = "部门管理"
                            rerun()
                    elif category == "岗位":
                        pos_name = item.get("name", item["type"])
                        st.write(f"- {pos_name}（{item['dept_name']}）")
                        if st.button("查看", key=f"search_pos_{item['id']}"):
                            st.session_state.active_tab = "岗位管理"
                            rerun()
                    elif category == "项目":
                        st.write(f"- {item['name']}（{item['status']}）")
                        if st.button("查看", key=f"search_proj_{item['id']}"):
                            st.session_state.active_main_nav = "项目管理"
                            st.session_state.active_proj_tab = "基础数据"
                            st.session_state.selected_project_id = item["id"]
                            rerun()

# 一级导航：系统管理 / 项目管理
main_nav = st.sidebar.radio(
    "系统导航",
    ["系统管理", "项目管理"],
    key="main_nav"
)

# ------------------------------
# 系统管理 -> 组织管理（保持不变）
# ------------------------------
if main_nav == "系统管理":
    st.subheader("🔧 系统管理")

    sys_sub_nav = st.sidebar.selectbox(
        "系统管理子模块",
        ["组织管理"],
        key="sys_sub_nav"
    )

    if sys_sub_nav == "组织管理":
        st.subheader("🏢 组织管理")

        col_batch = st.columns([4, 1, 1, 1])
        with col_batch[1]:
            import_btn = st.button("导入数据")
        with col_batch[2]:
            export_btn = st.button("导出数据")
        with col_batch[3]:
            st.download_button(
                "下载模板",
                data=export_to_excel(),
                file_name="组织数据模板.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        if export_btn:
            st.success("数据导出成功！")
            st.download_button(
                "保存Excel",
                data=export_to_excel(),
                file_name=f"组织数据_{datetime.now().strftime('%Y%m%d')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        org_tab = st.tabs(["部门管理", "岗位管理", "组织架构图"])

        # 1. 部门管理
        with org_tab[0]:
            st.header("部门管理")
            st.write("创建部门并管理人员（支持人员隶属多个部门）")

            col_dept_info, col_dept_employees = st.columns([1, 1])

            with col_dept_info:
                st.subheader("部门信息")
                dept_id = st.text_input("部门ID（留空自动生成）", placeholder="DEPT-001")
                dept_name = st.text_input("部门名称*", placeholder="如：研发部、市场部")
                dept_level = st.selectbox("部门层级", ["一级部门", "二级部门", "三级部门"])

                dept_options = ["无（顶级部门）"] + [d["name"] for d in st.session_state.departments.values()]
                parent_dept = st.selectbox("上级部门", dept_options)

                all_employees = ["暂未指定"] + [emp["name"] for emp in st.session_state.employees.values()]
                dept_manager = st.selectbox("部门负责人", all_employees)
                if dept_manager != "暂未指定" and st.button("查看负责人详情"):
                    for emp in st.session_state.employees.values():
                        if emp["name"] == dept_manager:
                            with st.expander(f"人员详情：{dept_manager}"):
                                st.write(f"**ID**：{emp['id']}")
                                st.write(f"**联系方式**：{emp['contact']}")
                                st.write(f"**所属部门**：{','.join(emp['dept_names'])}")
                            break

                dept_desc = st.text_area("部门描述", placeholder="描述部门核心职能...")
                dept_status = st.selectbox("部门状态", ["正常", "暂停", "解散"])

                if st.button("保存部门"):
                    if not dept_name.strip():
                        st.warning("部门名称为必填项！")
                    else:
                        if not dept_id.strip():
                            dept_id = generate_unique_id("DEPT")

                        parent_dept_id = None
                        if parent_dept != "无（顶级部门）":
                            for id, d in st.session_state.departments.items():
                                if d["name"] == parent_dept:
                                    parent_dept_id = id
                                    break

                        manager_id = None
                        if dept_manager != "暂未指定":
                            for emp_id, emp in st.session_state.employees.items():
                                if emp["name"] == dept_manager:
                                    manager_id = emp_id
                                    break

                        if dept_id not in st.session_state.departments:
                            st.session_state.departments[dept_id] = {"members": []}

                        st.session_state.departments[dept_id].update({
                            "id": dept_id, "name": dept_name.strip(), "level": dept_level,
                            "parent_dept": parent_dept, "parent_dept_id": parent_dept_id,
                            "manager": dept_manager, "manager_id": manager_id,
                            "description": dept_desc.strip(), "status": dept_status,
                            "create_time": get_current_time(), "update_time": get_current_time()
                        })
                        st.success(f"✅ 部门「{dept_name}」保存成功！")

            # 2. 部门人员管理
            with col_dept_employees:
                st.subheader("部门人员管理")

                if st.session_state.departments:
                    dept_selector = {d["name"]: d["id"] for d in st.session_state.departments.values()}
                    selected_dept_name = st.selectbox("选择部门", list(dept_selector.keys()))
                    selected_dept_id = dept_selector[selected_dept_name]

                    st.write("### 新增部门人员")
                    col_name, col_contact = st.columns(2)
                    with col_name:
                        new_emp_name = st.text_input("人员姓名*", key="new_emp_name")
                    with col_contact:
                        new_emp_contact = st.text_input("联系方式", key="new_emp_contact")
                    new_emp_title = st.text_input("职称", placeholder="如：高级工程师")

                    other_depts = [d["name"] for d in st.session_state.departments.values()
                                   if d["id"] != selected_dept_id]
                    if other_depts:
                        additional_depts = st.multiselect(
                            "同时隶属其他部门（可选）",
                            other_depts,
                            help="人员可同时属于多个部门"
                        )
                    else:
                        additional_depts = []
                        st.info("暂无其他部门可选择")

                    if st.button("添加到部门"):
                        if not new_emp_name.strip():
                            st.warning("人员姓名为必填项！")
                        else:
                            emp_id = generate_unique_id("EMP")
                            dept_ids = [selected_dept_id]
                            dept_names = [selected_dept_name]
                            for dept_name in additional_depts:
                                for id, d in st.session_state.departments.items():
                                    if d["name"] == dept_name:
                                        dept_ids.append(id)
                                        dept_names.append(dept_name)
                                        break

                            st.session_state.employees[emp_id] = {
                                "id": emp_id, "name": new_emp_name.strip(),
                                "contact": new_emp_contact.strip(), "title": new_emp_title.strip(),
                                "dept_ids": dept_ids, "dept_names": dept_names,
                                "status": "在职", "create_time": get_current_time()
                            }

                            for dept_id in dept_ids:
                                if emp_id not in st.session_state.departments[dept_id]["members"]:
                                    st.session_state.departments[dept_id]["members"].append(emp_id)

                            st.success(f"✅ 已添加「{new_emp_name}」到部门：{', '.join(dept_names)}")
                            rerun()

                if st.session_state.departments and selected_dept_id:
                    st.write("### 部门人员列表")
                    dept_members = get_dept_members(selected_dept_id)

                    if dept_members:
                        batch_remove = st.checkbox("批量移除")
                        selected_emp_ids = []

                        for emp_id, emp_name in dept_members:
                            emp = st.session_state.employees[emp_id]
                            with st.expander(f"{emp_name}（{emp['status']}）"):
                                if batch_remove:
                                    if st.checkbox(f"选择 {emp_name}", key=f"batch_{emp_id}"):
                                        selected_emp_ids.append(emp_id)

                                st.write(f"**联系方式**：{emp['contact'] or '未填写'}")
                                st.write(f"**职称**：{emp['title'] or '未填写'}")
                                st.write(f"**同时隶属**：{', '.join(emp['dept_names'])}")
                                st.write(f"**加入时间**：{emp['create_time']}")

                                emp_positions = []
                                for pos in st.session_state.positions.values():
                                    if emp_id in pos["employees"]:
                                        pos_name = pos.get("name", pos["type"])
                                        emp_positions.append(f"{pos_name}（{pos['dept_name']}）")
                                if emp_positions:
                                    st.write(f"**关联岗位**：{', '.join(emp_positions)}")

                                if st.button("从本部门移除", key=f"remove_emp_{emp_id}_{selected_dept_id}",
                                             type="secondary"):
                                    st.session_state.departments[selected_dept_id]["members"].remove(emp_id)
                                    emp["dept_ids"].remove(selected_dept_id)
                                    emp["dept_names"].remove(selected_dept_name)
                                    st.success(f"已将「{emp_name}」从「{selected_dept_name}」移除")
                                    rerun()

                        if batch_remove and selected_emp_ids:
                            if st.button("确认批量移除", type="primary"):
                                for emp_id in selected_emp_ids:
                                    st.session_state.departments[selected_dept_id]["members"].remove(emp_id)
                                    emp = st.session_state.employees[emp_id]
                                    emp["dept_ids"].remove(selected_dept_id)
                                    emp["dept_names"].remove(selected_dept_name)
                                st.success(f"已批量移除 {len(selected_emp_ids)} 名人员")
                                rerun()
                    else:
                        st.info("该部门暂无人员，请点击上方添加")

        # 3. 岗位管理
        with org_tab[1]:
            st.header("岗位管理")
            st.write("创建岗位（仅“职员”类型需要填写岗位名称）")

            col_pos_create, col_pos_list = st.columns([1, 1])

            with col_pos_create:
                st.subheader("创建岗位")
                pos_id = st.text_input("岗位ID（留空自动生成）", placeholder="POS-001")

                default_types = ["执行主管", "职能主管", "项目经理主管", "项目经理", "职员"]
                all_types = default_types + st.session_state.custom_position_types
                selected_type = st.selectbox("选择类型", all_types)

                pos_name = None
                if selected_type == "职员":
                    pos_name = st.text_input("岗位名称*", placeholder="如：前端开发工程师")

                with st.expander("+ 添加自定义类型"):
                    new_type = st.text_input("新类型名称")
                    if st.button("添加类型"):
                        if new_type.strip() and new_type not in all_types:
                            st.session_state.custom_position_types.append(new_type.strip())
                            st.success(f"已添加「{new_type}」")
                            rerun()

                if st.session_state.departments:
                    dept_options = {d["name"]: d["id"] for d in st.session_state.departments.values()}
                    selected_dept_name = st.selectbox("所属部门", list(dept_options.keys()))
                    selected_dept_id = dept_options[selected_dept_name]
                    if st.button("查看部门详情"):
                        dept = st.session_state.departments[selected_dept_id]
                        with st.expander(f"部门详情：{selected_dept_name}"):
                            st.write(f"**层级**：{dept['level']}")
                            st.write(f"**负责人**：{dept['manager']}")
                            st.write(f"**描述**：{dept['description']}")
                else:
                    st.warning("请先创建部门！")
                    selected_dept_id = None
                    selected_dept_name = None

                selected_emp_ids = []
                if st.session_state.employees:
                    emp_options = {emp["name"]: emp_id for emp_id, emp in st.session_state.employees.items()}
                    selected_emp_names = st.multiselect("选择岗位人员", list(emp_options.keys()))
                    selected_emp_ids = [emp_options[name] for name in selected_emp_names]

                pos_manager = "暂未指定"
                if selected_emp_ids:
                    manager_options = ["暂未指定"] + [get_employee_name(emp_id) for emp_id in selected_emp_ids]
                    pos_manager = st.selectbox("主责人员", manager_options)

                pos_skills = st.text_area("技能要求", placeholder="如：熟悉项目管理流程")
                pos_status = st.selectbox("岗位状态", ["正常", "空缺", "暂停招聘"])

                if st.button("保存岗位"):
                    if selected_type == "职员" and (not pos_name or not pos_name.strip()):
                        st.warning("“职员”类型必须填写岗位名称！")
                    elif not selected_dept_id:
                        st.warning("请选择所属部门！")
                    else:
                        if not pos_id.strip():
                            pos_id = generate_unique_id("POS")

                        manager_id = None
                        if pos_manager != "暂未指定":
                            for emp_id in selected_emp_ids:
                                if get_employee_name(emp_id) == pos_manager:
                                    manager_id = emp_id
                                    break

                        pos_data = {
                            "id": pos_id, "type": selected_type,
                            "dept_name": selected_dept_name, "dept_id": selected_dept_id,
                            "employees": selected_emp_ids,
                            "employees_names": [get_employee_name(emp_id) for emp_id in selected_emp_ids],
                            "manager": pos_manager, "manager_id": manager_id,
                            "skills": pos_skills.strip(), "status": pos_status,
                            "create_time": get_current_time()
                        }
                        if selected_type == "职员":
                            pos_data["name"] = pos_name.strip()

                        st.session_state.positions[pos_id] = pos_data
                        st.success(f"✅ 岗位「{pos_name if selected_type == '职员' else selected_type}」保存成功！")

            with col_pos_list:
                st.subheader("当前组织形式分析")
                org_form = judge_org_form()
                st.info(f"**当前项目管理组织形式**：{org_form}")

                form_desc = get_org_form_desc(org_form)
                with st.expander("查看组织形式详情"):
                    st.write(f"**优势**：{form_desc['优势']}")
                    st.write(f"**劣势**：{form_desc['劣势']}")
                    st.write(f"**适用项目类型**：{form_desc['适用']}")

                st.subheader("岗位列表")
                if st.session_state.departments:
                    filter_dept = st.selectbox("按部门筛选", ["全部"] + list(dept_options.keys()))
                else:
                    filter_dept = "全部"

                if st.session_state.positions:
                    filtered_positions = []
                    for pos in st.session_state.positions.values():
                        if filter_dept == "全部" or pos["dept_name"] == filter_dept:
                            filtered_positions.append(pos)

                    dept_groups = {}
                    for pos in filtered_positions:
                        dept_name = pos["dept_name"]
                        if dept_name not in dept_groups:
                            dept_groups[dept_name] = []
                        dept_groups[dept_name].append(pos)

                    for dept_name, positions in dept_groups.items():
                        st.write(f"### {dept_name}")
                        for pos in positions:
                            display_name = pos["name"] if pos["type"] == "职员" else pos["type"]
                            with st.expander(f"{display_name}（{pos['status']}）"):
                                st.write(f"**类型**：{pos['type']}")
                                st.write(f"**主责人员**：{pos['manager']}")
                                st.write(f"**岗位人员**：{', '.join(pos['employees_names'])}")
                                st.write(f"**技能要求**：{pos['skills'] or '无'}")

                                if st.button("查看所有人员详情", key=f"view_pos_emps_{pos['id']}", type="secondary"):
                                    for emp_id in pos["employees"]:
                                        emp = st.session_state.employees[emp_id]
                                        with st.expander(f"{emp['name']}"):
                                            st.write(f"**所属部门**：{','.join(emp['dept_names'])}")
                                            st.write(f"**联系方式**：{emp['contact']}")

                                if st.button("删除", key=f"del_pos_{pos['id']}", type="secondary"):
                                    del st.session_state.positions[pos['id']]
                                    st.success(f"已删除岗位「{display_name}」")
                                    rerun()
                else:
                    st.info("暂无岗位数据，请在左侧创建")

        # 4. 组织架构图
        with org_tab[2]:
            st.header("组织架构图")
            st.write("部门层级关系可视化（点击节点可展开/折叠，支持缩放）")

            fig = generate_org_chart()
            if fig:
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("暂无部门数据，请先在「部门管理」创建部门")

                if st.button("创建示例部门架构"):
                    dept1_id = generate_unique_id("DEPT")
                    st.session_state.departments[dept1_id] = {
                        "id": dept1_id, "name": "研发中心", "level": "一级部门",
                        "parent_dept": "无（顶级部门）", "parent_dept_id": None,
                        "manager": "张三", "manager_id": None,
                        "description": "负责公司所有产品研发", "status": "正常",
                        "create_time": get_current_time(), "update_time": get_current_time(),
                        "members": []
                    }

                    dept2_id = generate_unique_id("DEPT")
                    st.session_state.departments[dept2_id] = {
                        "id": dept2_id, "name": "前端开发部", "level": "二级部门",
                        "parent_dept": "研发中心", "parent_dept_id": dept1_id,
                        "manager": "李四", "manager_id": None,
                        "description": "负责前端开发", "status": "正常",
                        "create_time": get_current_time(), "update_time": get_current_time(),
                        "members": []
                    }
                    st.success("示例部门架构创建成功！请刷新页面查看")
                    rerun()


# ------------------------------
# 项目管理模块（包含PBS、WBS、CS、BS）
# ------------------------------
elif main_nav == "项目管理":
    st.subheader("📈 项目管理")

    # 项目管理一级子模块
    proj_main_tab = st.tabs(["基础数据", "计划编制", "进度检测", "进度监控"])

    # 1. 基础数据（简化）
    with proj_main_tab[0]:
        st.header("基础数据")
        st.write("项目基本信息维护")

        with st.expander("+ 创建新项目", expanded=True):
            col_proj1, col_proj2 = st.columns(2)
            with col_proj1:
                proj_name = st.text_input("项目名称*", placeholder="如：企业官网改版项目")
                proj_code = st.text_input("项目编号", placeholder="自动生成可留空")
            with col_proj2:
                proj_manager = st.selectbox(
                    "项目经理",
                    ["请选择"] + [emp["name"] for emp in st.session_state.employees.values()]
                )
                proj_status = st.selectbox("项目状态", ["规划中", "进行中", "已暂停", "已完成"])

            proj_desc = st.text_area("项目描述", placeholder="简要描述项目目标、范围等")

            if st.button("保存项目"):
                if not proj_name.strip():
                    st.warning("项目名称为必填项")
                elif proj_manager == "请选择":
                    st.warning("请选择项目经理")
                else:
                    proj_id = generate_unique_id("PROJ") if not proj_code.strip() else proj_code.strip()
                    manager_id = get_employee_id(proj_manager)

                    st.session_state.projects[proj_id] = {
                        "id": proj_id,
                        "name": proj_name.strip(),
                        "manager": proj_manager,
                        "manager_id": manager_id,
                        "status": proj_status,
                        "description": proj_desc.strip(),
                        "create_time": get_current_time(),
                        "create_date": get_current_date()
                    }
                    st.success(f"✅ 项目「{proj_name}」创建成功！")

        if st.session_state.projects:
            st.subheader("项目列表")
            proj_df = pd.DataFrame([{
                "项目ID": proj["id"],
                "项目名称": proj["name"],
                "项目经理": proj["manager"],
                "状态": proj["status"],
                "创建日期": proj["create_date"]
            } for proj in st.session_state.projects.values()])
            st.dataframe(proj_df, use_container_width=True)
            # ========== 基础数据 - 检测周期定义 ==========
            st.subheader("检测周期定义")
            st.markdown("---")

            # 初始化检测周期数据结构
            if "detection_cycles" not in st.session_state:
                st.session_state.detection_cycles = {}  # 格式: {cycle_id: {周期详情}}
            if "selected_proj_id" not in st.session_state:
                st.session_state.selected_proj_id = ""
            if "selected_proj_name" not in st.session_state:
                st.session_state.selected_proj_name = ""


            # 工具函数（内置兼容）
            def generate_unique_id(prefix="CYCLE"):
                import uuid
                return f"{prefix}_{uuid.uuid4().hex[:8]}"


            def get_current_date():
                from datetime import datetime
                return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


            # 1. 项目选择
            col_proj, col_refresh = st.columns([3, 1])
            with col_proj:
                # 获取所有项目列表
                project_list = st.session_state.get("projects", {})
                if project_list:
                    project_options = {p["name"]: p["id"] for p in project_list.values()}
                    selected_proj_name = st.selectbox(
                        "选择项目",
                        list(project_options.keys()),
                        key="cycle_proj_select",
                        help="为指定项目配置进度检测周期"
                    )
                    selected_proj_id = project_options[selected_proj_name]
                    st.session_state.selected_proj_id = selected_proj_id
                    st.session_state.selected_proj_name = selected_proj_name
                else:
                    st.warning("暂无项目数据，请先在项目管理中创建项目")
                    st.stop()

            with col_refresh:
                if st.button("刷新周期列表", type="secondary"):
                    def rerun():
                        try:
                            st.rerun()
                        except AttributeError:
                            st.experimental_rerun()


                    rerun()

            st.markdown("---")

            # 2. 新增/编辑周期配置
            tab1, tab2 = st.tabs(["📝 新增周期配置", "📋 周期列表管理"])

            with tab1:
                st.subheader("新增检测周期")

                # 获取选中项目的基本信息（工期）
                project_info = next((p for p in st.session_state.projects.values() if p["id"] == selected_proj_id),
                                    None)
                proj_start_date = None
                proj_end_date = None
                if project_info and "start_date" in project_info and "end_date" in project_info:
                    proj_start_date = project_info["start_date"]
                    proj_end_date = project_info["end_date"]

                with st.form(key="add_cycle_form"):
                    col1, col2 = st.columns(2)

                    with col1:
                        # 周期基本信息
                        cycle_name = st.text_input(
                            "周期配置名称*",
                            placeholder="如：XX项目-周度检测周期",
                            key="cycle_name"
                        )
                        cycle_type = st.selectbox(
                            "周期类型*",
                            ["按周", "按月", "按里程碑"],
                            key="cycle_type",
                            help="选择进度检测的时间粒度"
                        )
                        # 项目工期选择（自动填充项目已有工期，支持手动调整）
                        from datetime import datetime

                        default_start = datetime.strptime(proj_start_date,
                                                          "%Y-%m-%d") if proj_start_date else datetime.now()
                        default_end = datetime.strptime(proj_end_date, "%Y-%m-%d") if proj_end_date else datetime.now()

                        cycle_start = st.date_input(
                            "周期配置开始日期*",
                            value=default_start,
                            key="cycle_start"
                        )
                        cycle_end = st.date_input(
                            "周期配置结束日期*",
                            value=default_end,
                            key="cycle_end"
                        )

                    with col2:
                        # 责任人及规则配置
                        employee_list = [emp["name"] for emp in
                                         st.session_state.get("employees", {}).values()] if st.session_state.get(
                            "employees") else ["默认责任人"]
                        cycle_owner = st.selectbox(
                            "周期填报责任人*",
                            employee_list,
                            key="cycle_owner"
                        )
                        lock_rule = st.selectbox(
                            "数据锁定规则",
                            ["周期结束后自动锁定", "手动锁定"],
                            key="lock_rule",
                            help="锁定后无法修改周期数据"
                        )
                        cycle_note = st.text_area(
                            "备注说明",
                            placeholder="填写周期配置的补充说明...",
                            key="cycle_note"
                        )

                    # 提交按钮
                    submit_cycle = st.form_submit_button("生成周期配置", type="primary")

                    if submit_cycle:
                        # 校验必填项
                        if not cycle_name.strip():
                            st.warning("请填写周期配置名称")
                        elif cycle_start > cycle_end:
                            st.warning("结束日期不能早于开始日期")
                        else:
                            # 生成周期ID
                            cycle_id = generate_unique_id("CYCLE")

                            # 自动拆分周期（核心逻辑）
                            from datetime import timedelta

                            cycles_detail = []
                            current_date = cycle_start
                            cycle_index = 1

                            # 按周拆分
                            if cycle_type == "按周":
                                while current_date <= cycle_end:
                                    # 计算本周结束日期（周日）
                                    week_end = current_date + timedelta(days=6 - current_date.weekday())
                                    if week_end > cycle_end:
                                        week_end = cycle_end

                                    cycles_detail.append({
                                        "sub_cycle_id": generate_unique_id("SUB_CYCLE"),
                                        "sub_cycle_name": f"第{cycle_index}周",
                                        "sub_cycle_start": current_date.strftime("%Y-%m-%d"),
                                        "sub_cycle_end": week_end.strftime("%Y-%m-%d"),
                                        "status": "未开始",  # 未开始/进行中/已结束/已锁定
                                        "owner": cycle_owner
                                    })

                                    # 下一周开始
                                    current_date = week_end + timedelta(days=1)
                                    cycle_index += 1

                            # 按月拆分
                            elif cycle_type == "按月":
                                while current_date <= cycle_end:
                                    # 计算本月最后一天
                                    next_month = current_date.replace(day=28) + timedelta(days=4)
                                    month_end = next_month - timedelta(days=next_month.day)
                                    if month_end > cycle_end:
                                        month_end = cycle_end

                                    cycles_detail.append({
                                        "sub_cycle_id": generate_unique_id("SUB_CYCLE"),
                                        "sub_cycle_name": f"{current_date.year}年{current_date.month}月",
                                        "sub_cycle_start": current_date.strftime("%Y-%m-%d"),
                                        "sub_cycle_end": month_end.strftime("%Y-%m-%d"),
                                        "status": "未开始",
                                        "owner": cycle_owner
                                    })

                                    # 下月开始
                                    current_date = month_end + timedelta(days=1)
                                    cycle_index += 1

                            # 按里程碑（暂简化为手动输入，可后续关联WBS里程碑）
                            elif cycle_type == "按里程碑":
                                cycles_detail.append({
                                    "sub_cycle_id": generate_unique_id("SUB_CYCLE"),
                                    "sub_cycle_name": "里程碑1",
                                    "sub_cycle_start": cycle_start.strftime("%Y-%m-%d"),
                                    "sub_cycle_end": cycle_end.strftime("%Y-%m-%d"),
                                    "status": "未开始",
                                    "owner": cycle_owner
                                })

                            # 保存周期配置
                            st.session_state.detection_cycles[cycle_id] = {
                                "id": cycle_id,
                                "name": cycle_name.strip(),
                                "project_id": selected_proj_id,
                                "project_name": selected_proj_name,
                                "type": cycle_type,
                                "start_date": cycle_start.strftime("%Y-%m-%d"),
                                "end_date": cycle_end.strftime("%Y-%m-%d"),
                                "owner": cycle_owner,
                                "lock_rule": lock_rule,
                                "note": cycle_note.strip(),
                                "create_time": get_current_date(),
                                "cycles_detail": cycles_detail,  # 拆分后的子周期列表
                                "status": "已生效"  # 已生效/已停用
                            }

                            st.success(f"成功生成{cycle_type}周期配置！共拆分出{len(cycles_detail)}个检测周期")


                            def rerun():
                                try:
                                    st.rerun()
                                except AttributeError:
                                    st.experimental_rerun()


                            rerun()

            with tab2:
                st.subheader("周期列表管理")

                # 筛选当前项目的周期配置
                project_cycles = [
                    cycle for cycle in st.session_state.detection_cycles.values()
                    if cycle["project_id"] == selected_proj_id
                ]

                if not project_cycles:
                    st.info("当前项目暂无检测周期配置，请先在「新增周期配置」中创建")
                else:
                    # 周期配置列表
                    cycle_table = []
                    for idx, cycle in enumerate(project_cycles, 1):
                        cycle_table.append({
                            "序号": idx,
                            "周期配置名称": cycle["name"],
                            "周期类型": cycle["type"],
                            "时间范围": f"{cycle['start_date']} 至 {cycle['end_date']}",
                            "责任人": cycle["owner"],
                            "子周期数量": len(cycle["cycles_detail"]),
                            "状态": cycle["status"],
                            "创建时间": cycle["create_time"],
                            "操作ID": cycle["id"]
                        })

                    import pandas as pd

                    df_cycles = pd.DataFrame(cycle_table)
                    edited_df = st.data_editor(
                        df_cycles.drop(columns=["操作ID"]),
                        use_container_width=True,
                        column_config={
                            "序号": st.column_config.NumberColumn(width="small"),
                            "周期配置名称": st.column_config.TextColumn(width="medium"),
                            "周期类型": st.column_config.TextColumn(width="small"),
                            "时间范围": st.column_config.TextColumn(width="medium"),
                            "责任人": st.column_config.TextColumn(width="small"),
                            "子周期数量": st.column_config.NumberColumn(width="small"),
                            "状态": st.column_config.SelectboxColumn(
                                "状态",
                                width="small",
                                options=["已生效", "已停用"],
                                required=True
                            ),
                            "创建时间": st.column_config.TextColumn(width="medium")
                        },
                        key="cycle_list_editor"
                    )

                    # 保存状态更新
                    col_save, col_export = st.columns([1, 1])
                    with col_save:
                        if st.button("保存状态修改", type="secondary"):
                            name_to_id = {cycle["name"]: cycle["id"] for cycle in project_cycles}
                            for _, row in edited_df.iterrows():
                                cycle_id = name_to_id.get(row["周期配置名称"])
                                if cycle_id:
                                    st.session_state.detection_cycles[cycle_id]["status"] = row["状态"]
                                    st.session_state.detection_cycles[cycle_id]["update_time"] = get_current_date()
                            st.success("周期配置状态已更新！")


                            def rerun():
                                try:
                                    st.rerun()
                                except AttributeError:
                                    st.experimental_rerun()


                            rerun()

                    # 导出周期配置
                    with col_export:
                        if st.button("导出周期配置", type="secondary"):
                            # 导出详细数据
                            export_data = []
                            for cycle in project_cycles:
                                for sub_cycle in cycle["cycles_detail"]:
                                    export_data.append({
                                        "项目名称": cycle["project_name"],
                                        "周期配置名称": cycle["name"],
                                        "子周期名称": sub_cycle["sub_cycle_name"],
                                        "子周期开始时间": sub_cycle["sub_cycle_start"],
                                        "子周期结束时间": sub_cycle["sub_cycle_end"],
                                        "责任人": sub_cycle["owner"],
                                        "状态": sub_cycle["status"]
                                    })

                            df_export = pd.DataFrame(export_data)


                            def export_to_excel(df, filename):
                                import io
                                buffer = io.BytesIO()
                                with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                                    df.to_excel(writer, index=False, sheet_name='检测周期配置')
                                buffer.seek(0)
                                st.download_button(
                                    label="下载Excel文件",
                                    data=buffer,
                                    file_name=f"{filename}.xlsx",
                                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                                )


                            export_to_excel(df_export,
                                            f"{selected_proj_name}_检测周期配置_{get_current_date().split(' ')[0]}")

                    st.markdown("---")

                    # 查看子周期详情
                    st.subheader("子周期详情")
                    selected_cycle_name = st.selectbox(
                        "选择周期配置",
                        [cycle["name"] for cycle in project_cycles],
                        key="sub_cycle_select"
                    )
                    selected_cycle = next(cycle for cycle in project_cycles if cycle["name"] == selected_cycle_name)

                    # 子周期列表
                    sub_cycle_table = []
                    for idx, sub_cycle in enumerate(selected_cycle["cycles_detail"], 1):
                        sub_cycle_table.append({
                            "序号": idx,
                            "子周期名称": sub_cycle["sub_cycle_name"],
                            "开始时间": sub_cycle["sub_cycle_start"],
                            "结束时间": sub_cycle["sub_cycle_end"],
                            "责任人": sub_cycle["owner"],
                            "状态": sub_cycle["status"],
                            "操作ID": sub_cycle["sub_cycle_id"]
                        })

                    df_sub_cycles = pd.DataFrame(sub_cycle_table)
                    st.data_editor(
                        df_sub_cycles.drop(columns=["操作ID"]),
                        use_container_width=True,
                        disabled=["序号", "子周期名称", "开始时间", "结束时间", "责任人"],
                        column_config={
                            "序号": st.column_config.NumberColumn(width="small"),
                            "子周期名称": st.column_config.TextColumn(width="medium"),
                            "开始时间": st.column_config.TextColumn(width="medium"),
                            "结束时间": st.column_config.TextColumn(width="medium"),
                            "责任人": st.column_config.TextColumn(width="small"),
                            "状态": st.column_config.SelectboxColumn(
                                "状态",
                                width="small",
                                options=["未开始", "进行中", "已结束", "已锁定"],
                                required=True
                            )
                        },
                        key="sub_cycle_editor"
                    )

                    # 保存子周期状态
                    if st.button("保存子周期状态", type="secondary"):
                        name_to_id = {sub["sub_cycle_name"]: sub["sub_cycle_id"] for sub in
                                      selected_cycle["cycles_detail"]}
                        for _, row in df_sub_cycles.iterrows():
                            sub_cycle_id = name_to_id.get(row["子周期名称"])
                            if sub_cycle_id:
                                # 找到对应子周期并更新状态
                                for sub in selected_cycle["cycles_detail"]:
                                    if sub["sub_cycle_id"] == sub_cycle_id:
                                        sub["status"] = row["状态"]
                                        break
                        # 保存到session_state
                        st.session_state.detection_cycles[selected_cycle["id"]]["cycles_detail"] = selected_cycle[
                            "cycles_detail"]
                        st.success("子周期状态已更新！")


                        def rerun():
                            try:
                                st.rerun()
                            except AttributeError:
                                st.experimental_rerun()


                        rerun()
    # 2. 计划编制（包含PBS、WBS、CS、BS）
    with proj_main_tab[1]:
        st.header("计划编制")

        # 计划编制二级子目录
        plan_sub_tab = st.tabs([
            "PBS定义", "WBS维护", "计划编制（CS）", "计划编制（BS）",
            "审批记录", "回收记录", "统筹计划"
        ])

        # ------------------------------
        # 2.1 PBS定义
        # ------------------------------
        with plan_sub_tab[0]:
            st.subheader("PBS定义（产品分解结构）")
            st.write("将项目交付成果分解为可管理的产品单元，支持多级嵌套")

            # 步骤1：选择项目
            if not st.session_state.projects:
                st.warning("请先在「基础数据」创建项目")
            else:
                project_options = {proj["name"]: proj["id"] for proj in st.session_state.projects.values()}
                selected_proj_name = st.selectbox("选择项目", list(project_options.keys()))
                selected_proj_id = project_options[selected_proj_name]
                selected_proj = st.session_state.projects[selected_proj_id]

                with st.expander("项目信息", expanded=False):
                    st.write(f"**项目ID**：{selected_proj['id']}")
                    st.write(f"**项目经理**：{selected_proj['manager']}")
                    st.write(f"**状态**：{selected_proj['status']}")

                # 步骤2：创建计划按钮（一级/二级区分）
                col_create = st.columns([1, 1])
                with col_create[0]:
                    # 新建一级计划（无需选择父节点）
                    if st.button("➕ 新建一级计划", type="primary"):
                        # 生成新节点ID
                        new_pbs_id = generate_unique_id("PBS")
                        # 生成PBS编号（自动递增：01, 02, 03...）
                        existing_first_level = [pbs for pbs in st.session_state.pbs_data.values()
                                                if pbs["project_id"] == selected_proj_id and pbs["level"] == "一级"]
                        new_code = f"{len(existing_first_level) + 1:02d}"  # 两位数编号

                        st.session_state.pbs_data[new_pbs_id] = {
                            "id": new_pbs_id,
                            "code": new_code,  # 改为自动生成的编号
                            "name": f"一级计划 {new_code}",
                            "project_id": selected_proj_id,
                            "project_name": selected_proj_name,
                            "parent_id": None,
                            "parent_name": None,
                            "start_date": get_current_date(),
                            "end_date": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"),
                            "plan_type": "未选择",
                            "level": "一级",
                            "responsible": selected_proj["manager"],  # 默认项目经理
                            "responsible_id": selected_proj["manager_id"],
                            "creator": selected_proj["manager"],
                            "creator_id": selected_proj["manager_id"],
                            "create_date": get_current_date(),
                            "日历": "7天工作制",
                            "作业数": 0
                        }
                        refresh_pbs_作业数()
                        st.success(f"一级计划 {new_code} 已创建，请在表格中编辑详情")
                        rerun()

                with col_create[1]:
                    # 新建二级计划（需选择一级计划作为父节点）
                    first_level_pbs = [pbs for pbs in st.session_state.pbs_data.values()
                                       if pbs["project_id"] == selected_proj_id and pbs["level"] == "一级"]

                    if first_level_pbs:
                        parent_options = {f"{pbs['name']}（{pbs['code']}）": pbs["id"] for pbs in first_level_pbs}
                        selected_parent_text = st.selectbox(
                            "选择父级一级计划",
                            list(parent_options.keys()),
                            key="pbs_parent_selector"
                        )
                        if st.button("➕ 新建二级计划", type="primary"):
                            parent_id = parent_options[selected_parent_text]
                            parent_pbs = st.session_state.pbs_data[parent_id]

                            new_pbs_id = generate_unique_id("PBS")
                            # 生成二级编号（父级编号 + .01/.02...）
                            existing_second_level = get_pbs_children(parent_id)
                            new_code = f"{parent_pbs['code']}.{len(existing_second_level) + 1:02d}"

                            st.session_state.pbs_data[new_pbs_id] = {
                                "id": new_pbs_id,
                                "code": new_code,
                                "name": f"二级计划 {new_code}",
                                "project_id": selected_proj_id,
                                "project_name": selected_proj_name,
                                "parent_id": parent_id,
                                "parent_name": parent_pbs["name"],
                                "start_date": parent_pbs["start_date"],
                                "end_date": parent_pbs["end_date"],
                                "plan_type": "未选择",
                                "level": "二级",
                                "responsible": selected_proj["manager"],
                                "responsible_id": selected_proj["manager_id"],
                                "creator": selected_proj["manager"],
                                "creator_id": selected_proj["manager_id"],
                                "create_date": get_current_date(),
                                "日历": parent_pbs["日历"],
                                "作业数": 0
                            }
                            refresh_pbs_作业数()
                            st.success(f"已为「{parent_pbs['name']}」创建二级计划 {new_code}")
                            rerun()
                    else:
                        st.info("请先创建一级计划")

                # 步骤3：展示PBS表格
                st.subheader("PBS计划列表")
                project_pbs = [pbs for pbs in st.session_state.pbs_data.values() if
                               pbs["project_id"] == selected_proj_id]

                if project_pbs:
                    # 准备表格数据
                    project_pbs_sorted = sorted(project_pbs, key=lambda x: (x["level"], x["code"]))
                    pbs_table_data = []

                    for idx, pbs in enumerate(project_pbs_sorted, 1):
                        # 二级计划名称前加缩进符号
                        display_name = pbs["name"] if pbs["level"] == "一级" else f"└─ {pbs['name']}"

                        # 转换日期为datetime对象
                        try:
                            start_date = datetime.strptime(pbs["start_date"], "%Y-%m-%d")
                            end_date = datetime.strptime(pbs["end_date"], "%Y-%m-%d")
                        except:
                            start_date = datetime.now()
                            end_date = datetime.now() + timedelta(days=7)

                        pbs_table_data.append({
                            "序号": idx,
                            "编号": pbs["code"],
                            "名称": display_name,
                            "设定开始": start_date,
                            "设定完成": end_date,
                            "计划类型": pbs["plan_type"],
                            "等级": pbs["level"],
                            "责任人": pbs["responsible"],
                            "创建人": pbs["creator"],
                            "创建日期": pbs["create_date"],
                            "日历": pbs["日历"],
                            "作业数": pbs["作业数"],
                            "操作": pbs["id"]
                        })

                    # 展示表格
                    pbs_df = pd.DataFrame(pbs_table_data)
                    st.markdown("""<style>
                        .dataframe th, .dataframe td {font-size: 12px !important; padding: 4px 8px !important;}
                    </style>""", unsafe_allow_html=True)

                    edited_df = st.data_editor(
                        pbs_df.drop(columns=["操作"]),
                        num_rows="dynamic",
                        use_container_width=True,
                        column_config={
                            "序号": st.column_config.NumberColumn(width="small"),
                            "编号": st.column_config.TextColumn(width="small", disabled=True),  # 编号不可编辑
                            "名称": st.column_config.TextColumn(width="medium"),
                            "设定开始": st.column_config.DateColumn(
                                width="small",
                                format="YYYY-MM-DD"
                            ),
                            "设定完成": st.column_config.DateColumn(
                                width="small",
                                format="YYYY-MM-DD"
                            ),
                            "计划类型": st.column_config.SelectboxColumn(
                                options=["未选择", "设计类", "开发类", "测试类", "部署类", "其他"],
                                width="small"
                            ),
                            "等级": st.column_config.TextColumn(width="small", disabled=True),
                            "责任人": st.column_config.SelectboxColumn(
                                options=[emp["name"] for emp in st.session_state.employees.values()],
                                width="small"
                            ),
                            "创建人": st.column_config.TextColumn(width="small", disabled=True),
                            "创建日期": st.column_config.TextColumn(width="small", disabled=True),
                            "日历": st.column_config.SelectboxColumn(
                                options=["5天工作制", "6天工作制", "7天工作制"],
                                width="small"
                            ),
                            "作业数": st.column_config.NumberColumn(width="small", disabled=True)
                        },
                        key="pbs_editor"
                    )

                    # 保存编辑结果
                    if st.button("💾 保存编辑", type="secondary"):
                        code_to_id = {pbs["code"]: pbs["id"] for pbs in project_pbs}

                        for _, row in edited_df.iterrows():
                            pbs_id = code_to_id.get(row["编号"])
                            if pbs_id and pbs_id in st.session_state.pbs_data:
                                start_date = row["设定开始"].strftime("%Y-%m-%d") if isinstance(row["设定开始"],
                                                                                                datetime) else row[
                                    "设定开始"]
                                end_date = row["设定完成"].strftime("%Y-%m-%d") if isinstance(row["设定完成"],
                                                                                              datetime) else row[
                                    "设定完成"]

                                st.session_state.pbs_data[pbs_id].update({
                                    "name": row["名称"].replace("└─ ", ""),
                                    "start_date": start_date,
                                    "end_date": end_date,
                                    "plan_type": row["计划类型"],
                                    "responsible": row["责任人"],
                                    "responsible_id": get_employee_id(row["责任人"]),
                                    "日历": row["日历"]
                                })

                        refresh_pbs_作业数()
                        st.success("✅ 编辑内容已保存")

                    # 删除功能
                    with st.expander("🗑️ 批量删除"):
                        pbs_to_delete = st.multiselect(
                            "选择要删除的计划",
                            [f"{pbs['name']}（{pbs['code']}）" for pbs in project_pbs]
                        )
                        if pbs_to_delete and st.button("确认删除选中项", type="primary"):
                            code_to_id = {pbs["code"]: pbs["id"] for pbs in project_pbs}
                            deleted_count = 0

                            for item in pbs_to_delete:
                                pbs_code = item.split("（")[-1].replace("）", "")
                                pbs_id = code_to_id.get(pbs_code)

                                if pbs_id:
                                    # 级联删除子节点
                                    children = get_pbs_children(pbs_id)
                                    for child in children:
                                        del st.session_state.pbs_data[child["id"]]
                                        deleted_count += 1

                                    # 删除当前节点
                                    del st.session_state.pbs_data[pbs_id]
                                    deleted_count += 1

                            refresh_pbs_作业数()
                            st.success(f"✅ 已删除 {deleted_count} 个计划（含子计划）")
                            rerun()
                else:
                    st.info("该项目暂无PBS计划，请点击上方创建一级计划")

        # ------------------------------
        # 2.2 WBS维护
        # ------------------------------
        with plan_sub_tab[1]:
            # WBS介绍说明
            st.subheader("WBS维护（工作分解结构）")
            with st.expander("什么是WBS？", expanded=True):
                st.write("""
                工作分解结构（WBS）是项目范围管理的一种技术手段，通过一种逐层分解的结构化编码，
                将项目工作内容逐级分解成较小的、易于管理的单元或工作包。大大增强项目进度和成本管理的精细化能力。

                ★ 操作步骤：
                ◎ 创建主计划WBS（关联PBS节点）
                ◎ 创建子计划的WBS（基于主计划进一步分解）
                """)

            # 步骤1：选择项目
            if not st.session_state.projects:
                st.warning("请先在「基础数据」创建项目")
            else:
                project_options = {proj["name"]: proj["id"] for proj in st.session_state.projects.values()}
                selected_proj_name = st.selectbox("选择项目", list(project_options.keys()), key="wbs_proj_select")
                selected_proj_id = project_options[selected_proj_name]

                # 步骤2：选择关联的PBS节点
                project_pbs = [pbs for pbs in st.session_state.pbs_data.values() if
                               pbs["project_id"] == selected_proj_id]
                if not project_pbs:
                    st.warning("请先在「PBS定义」中创建PBS计划")
                else:
                    pbs_options = {f"{pbs['name']}（{pbs['code']}）": pbs["id"] for pbs in project_pbs}
                    selected_pbs_text = st.selectbox("选择关联的PBS节点", list(pbs_options.keys()),
                                                     key="wbs_pbs_select")
                    selected_pbs_id = pbs_options[selected_pbs_text]
                    selected_pbs = st.session_state.pbs_data[selected_pbs_id]

                    with st.expander("关联PBS信息", expanded=False):
                        st.write(f"**PBS编号**：{selected_pbs['code']}")
                        st.write(f"**PBS名称**：{selected_pbs['name']}")
                        st.write(f"**负责人**：{selected_pbs['responsible']}")
                        st.write(f"**时间范围**：{selected_pbs['start_date']} 至 {selected_pbs['end_date']}")

                # 步骤3：创建WBS按钮（主计划/子计划）
                if project_pbs:  # 确保已选择PBS
                    col_wbs_create = st.columns([1, 1])
                    with col_wbs_create[0]:
                        # 新建主计划WBS（关联PBS）
                        if st.button("➕ 创建主计划WBS", type="primary"):
                            new_wbs_id = generate_unique_id("WBS")
                            # 生成结构化编号（PBS编号 + .A/B/C...）
                            new_code = generate_wbs_code(pbs_id=selected_pbs_id)

                            st.session_state.wbs_data[new_wbs_id] = {
                                "id": new_wbs_id,
                                "code": new_code,
                                "name": f"主计划WBS {new_code}",
                                "pbs_id": selected_pbs_id,
                                "pbs_code": selected_pbs["code"],
                                "pbs_name": selected_pbs["name"],
                                "project_id": selected_proj_id,
                                "project_name": selected_proj_name,
                                "parent_id": None,  # 主计划无父节点
                                "parent_name": None,
                                "start_date": selected_pbs["start_date"],
                                "end_date": selected_pbs["end_date"],
                                "task_type": "未选择",  # 任务类型
                                "responsible": selected_pbs["responsible"],  # 默认继承PBS负责人
                                "responsible_id": selected_pbs["responsible_id"],
                                "creator": selected_pbs["creator"],
                                "creator_id": selected_pbs["creator_id"],
                                "create_date": get_current_date(),
                                "任务数": 0  # 子任务数量
                            }
                            refresh_wbs_任务数()
                            st.success(f"主计划WBS {new_code} 已创建")
                            rerun()

                    with col_wbs_create[1]:
                        # 新建子计划WBS（基于主计划）
                        pbs_wbs_list = get_pbs_wbs_list(selected_pbs_id)
                        if pbs_wbs_list:
                            parent_wbs_options = {f"{wbs['name']}（{wbs['code']}）": wbs["id"] for wbs in pbs_wbs_list}
                            selected_parent_wbs_text = st.selectbox(
                                "选择父级WBS",
                                list(parent_wbs_options.keys()),
                                key="wbs_parent_select"
                            )
                            if st.button("➕ 创建子计划WBS", type="primary"):
                                parent_wbs_id = parent_wbs_options[selected_parent_wbs_text]
                                parent_wbs = st.session_state.wbs_data[parent_wbs_id]

                                new_wbs_id = generate_unique_id("WBS")
                                # 生成子计划编号（父级编号 + .1/2/3...）
                                new_code = generate_wbs_code(parent_id=parent_wbs_id)

                                st.session_state.wbs_data[new_wbs_id] = {
                                    "id": new_wbs_id,
                                    "code": new_code,
                                    "name": f"子计划WBS {new_code}",
                                    "pbs_id": selected_pbs_id,
                                    "pbs_code": selected_pbs["code"],
                                    "pbs_name": selected_pbs["name"],
                                    "project_id": selected_proj_id,
                                    "project_name": selected_proj_name,
                                    "parent_id": parent_wbs_id,
                                    "parent_name": parent_wbs["name"],
                                    "start_date": parent_wbs["start_date"],
                                    "end_date": parent_wbs["end_date"],
                                    "task_type": "未选择",
                                    "responsible": parent_wbs["responsible"],  # 继承父级负责人
                                    "responsible_id": parent_wbs["responsible_id"],
                                    "creator": parent_wbs["creator"],
                                    "creator_id": parent_wbs["creator_id"],
                                    "create_date": get_current_date(),
                                    "任务数": 0
                                }
                                refresh_wbs_任务数()
                                st.success(f"已为「{parent_wbs['name']}」创建子计划WBS {new_code}")
                                rerun()
                        else:
                            st.info("请先创建主计划WBS")

                # 步骤4：展示WBS表格
                st.subheader("WBS任务列表")
                if project_pbs and selected_pbs_id:
                    wbs_list = get_pbs_wbs_list(selected_pbs_id)

                    if wbs_list:
                        # 按层级和编号排序
                        wbs_sorted = sorted(wbs_list, key=lambda x: (x["code"].count("."), x["code"]))
                        wbs_table_data = []

                        for idx, wbs in enumerate(wbs_sorted, 1):
                            # 层级缩进显示（主计划无缩进，子计划加└─）
                            level = wbs["code"].count(".")  # 按点的数量判断层级
                            indent = "└─ " * (level - 1) if level > 1 else ""
                            display_name = f"{indent}{wbs['name']}"

                            # 转换日期为datetime对象
                            try:
                                start_date = datetime.strptime(wbs["start_date"], "%Y-%m-%d")
                                end_date = datetime.strptime(wbs["end_date"], "%Y-%m-%d")
                            except:
                                start_date = datetime.now()
                                end_date = datetime.now() + timedelta(days=3)

                            wbs_table_data.append({
                                "序号": idx,
                                "编号": wbs["code"],
                                "名称": display_name,
                                "设定开始": start_date,
                                "设定完成": end_date,
                                "任务类型": wbs["task_type"],
                                "负责人": wbs["responsible"],
                                "创建人": wbs["creator"],
                                "创建日期": wbs["create_date"],
                                "子任务数": wbs["任务数"],
                                "操作": wbs["id"]
                            })

                        # 展示表格
                        wbs_df = pd.DataFrame(wbs_table_data)
                        st.markdown("""<style>
                            .dataframe th, .dataframe td {font-size: 12px !important; padding: 4px 8px !important;}
                        </style>""", unsafe_allow_html=True)

                        edited_wbs_df = st.data_editor(
                            wbs_df.drop(columns=["操作"]),
                            num_rows="dynamic",
                            use_container_width=True,
                            column_config={
                                "序号": st.column_config.NumberColumn(width="small"),
                                "编号": st.column_config.TextColumn(width="small", disabled=True),  # 编号不可编辑
                                "名称": st.column_config.TextColumn(width="medium"),
                                "设定开始": st.column_config.DateColumn(
                                    width="small",
                                    format="YYYY-MM-DD"
                                ),
                                "设定完成": st.column_config.DateColumn(
                                    width="small",
                                    format="YYYY-MM-DD"
                                ),
                                "任务类型": st.column_config.SelectboxColumn(
                                    options=["未选择", "需求分析", "设计开发", "测试验证", "部署上线", "文档编写",
                                             "其他"],
                                    width="small"
                                ),
                                "负责人": st.column_config.SelectboxColumn(
                                    options=[emp["name"] for emp in st.session_state.employees.values()],
                                    width="small"
                                ),
                                "创建人": st.column_config.TextColumn(width="small", disabled=True),
                                "创建日期": st.column_config.TextColumn(width="small", disabled=True),
                                "子任务数": st.column_config.NumberColumn(width="small", disabled=True)
                            },
                            key="wbs_editor"
                        )

                        # 保存编辑结果
                        if st.button("💾 保存WBS编辑", type="secondary"):
                            code_to_id = {wbs["code"]: wbs["id"] for wbs in wbs_list}

                            for _, row in edited_wbs_df.iterrows():
                                wbs_id = code_to_id.get(row["编号"])
                                if wbs_id and wbs_id in st.session_state.wbs_data:
                                    start_date = row["设定开始"].strftime("%Y-%m-%d") if isinstance(row["设定开始"],
                                                                                                    datetime) else row[
                                        "设定开始"]
                                    end_date = row["设定完成"].strftime("%Y-%m-%d") if isinstance(row["设定完成"],
                                                                                                  datetime) else row[
                                        "设定完成"]

                                    # 去除缩进符号
                                    level = row["编号"].count(".")
                                    indent = "└─ " * (level - 1) if level > 1 else ""
                                    clean_name = row["名称"].replace(indent, "")

                                    st.session_state.wbs_data[wbs_id].update({
                                        "name": clean_name,
                                        "start_date": start_date,
                                        "end_date": end_date,
                                        "task_type": row["任务类型"],
                                        "responsible": row["负责人"],
                                        "responsible_id": get_employee_id(row["负责人"])
                                    })

                            refresh_wbs_任务数()
                            st.success("✅ WBS编辑内容已保存")

                        # 删除功能
                        with st.expander("🗑️ 批量删除WBS"):
                            wbs_to_delete = st.multiselect(
                                "选择要删除的WBS任务",
                                [f"{wbs['name']}（{wbs['code']}）" for wbs in wbs_list]
                            )
                            if wbs_to_delete and st.button("确认删除选中WBS", type="primary"):
                                code_to_id = {wbs["code"]: wbs["id"] for wbs in wbs_list}
                                deleted_count = 0

                                for item in wbs_to_delete:
                                    wbs_code = item.split("（")[-1].replace("）", "")
                                    wbs_id = code_to_id.get(wbs_code)

                                    if wbs_id:
                                        # 级联删除子节点
                                        children = get_wbs_children(wbs_id)
                                        for child in children:
                                            del st.session_state.wbs_data[child["id"]]
                                            deleted_count += 1

                                        # 删除当前节点
                                        del st.session_state.wbs_data[wbs_id]
                                        deleted_count += 1

                                refresh_wbs_任务数()
                                st.success(f"✅ 已删除 {deleted_count} 个WBS任务（含子任务）")
                                rerun()
                    else:
                        st.info("该PBS节点暂无WBS任务，请点击上方创建主计划WBS")

        # ------------------------------
        # 2.3 计划编制（CS，关键路径法）- 完整支持FS/SS/FF/SF依赖
        # 核心逻辑：根据依赖类型动态计算ES/EF/LS/LF，确保关键路径符合CPM定义
        # ------------------------------
        with plan_sub_tab[2]:
            st.subheader("计划编制/CS（关键路径法）")
            st.write("""
            支持四种任务依赖类型，关键路径计算遵循以下规则：  
            1. **FS（完成→开始）**：前置任务完成后，本任务才能开始  
            2. **SS（开始→开始）**：前置任务开始后，本任务才能开始  
            3. **FF（完成→完成）**：前置任务完成后，本任务才能完成  
            4. **SF（开始→完成）**：前置任务开始后，本任务才能完成  
            关键路径是总浮动时间=0的任务链，决定项目最短工期。
            """)

            # 选择项目
            if not st.session_state.projects:
                st.warning("请先在「基础数据」创建项目")
            else:
                project_options = {proj["name"]: proj["id"] for proj in st.session_state.projects.values()}
                selected_proj_name = st.selectbox("选择项目", list(project_options.keys()), key="cs_proj_select")
                selected_proj_id = project_options[selected_proj_name]

                # 选择关联的PBS
                project_pbs = [pbs for pbs in st.session_state.pbs_data.values() if
                               pbs["project_id"] == selected_proj_id]
                if not project_pbs:
                    st.warning("请先在「PBS定义」中创建PBS计划")
                else:
                    pbs_options = {f"{pbs['name']}（{pbs['code']}）": pbs["id"] for pbs in project_pbs}
                    selected_pbs_text = st.selectbox("选择关联的PBS节点", list(pbs_options.keys()), key="cs_pbs_select")
                    selected_pbs_id = pbs_options[selected_pbs_text]
                    selected_pbs = st.session_state.pbs_data[selected_pbs_id]

                # 新建CS计划
                if project_pbs:
                    if st.button("➕ 新建CS计划", type="primary"):
                        cs_id = generate_unique_id("CS")
                        st.session_state.cs_plans[cs_id] = {
                            "id": cs_id,
                            "project_id": selected_proj_id,
                            "project_name": selected_proj_name,
                            "pbs_id": selected_pbs_id,
                            "pbs_name": selected_pbs["name"],
                            "start_date": selected_pbs["start_date"],
                            "end_date": selected_pbs["end_date"],
                            "create_date": get_current_date(),
                            "tasks": []
                        }
                        st.success(f"CS计划已创建，时间范围：{selected_pbs['start_date']} 至 {selected_pbs['end_date']}")
                        rerun()

                # 选择CS计划
                if st.session_state.cs_plans:
                    cs_options = {f"CS计划-{cs['id']}（{cs['project_name']}-{cs['pbs_name']}）": cs["id"]
                                  for cs in st.session_state.cs_plans.values() if cs["project_id"] == selected_proj_id}
                    if cs_options:
                        selected_cs_text = st.selectbox("选择CS计划", list(cs_options.keys()), key="cs_plan_select")
                        selected_cs_id = cs_options[selected_cs_text]
                        selected_cs = st.session_state.cs_plans[selected_cs_id]

                        # 计划时间范围编辑
                        col_date1, col_date2 = st.columns(2)
                        with col_date1:
                            plan_start = st.date_input(
                                "计划开始日期",
                                value=datetime.strptime(selected_cs["start_date"], "%Y-%m-%d"),
                                key="cs_plan_start"
                            )
                        with col_date2:
                            plan_end = st.date_input(
                                "计划结束日期",
                                value=datetime.strptime(selected_cs["end_date"], "%Y-%m-%d"),
                                key="cs_plan_end"
                            )
                        if st.button("更新计划时间范围", type="secondary"):
                            if plan_start > plan_end:
                                st.warning("开始日期不能晚于结束日期")
                            else:
                                st.session_state.cs_plans[selected_cs_id]["start_date"] = plan_start.strftime(
                                    "%Y-%m-%d")
                                st.session_state.cs_plans[selected_cs_id]["end_date"] = plan_end.strftime("%Y-%m-%d")
                                st.success(f"时间范围更新为：{plan_start} 至 {plan_end}")

                        # 新增任务
                        with st.expander("+ 新增任务", expanded=False):
                            task_id = generate_unique_id("TASK")
                            task_name = st.text_input("任务名称*", key="cs_task_name")

                            # 任务时间设置
                            col_task1, col_task2 = st.columns(2)
                            with col_task1:
                                task_start = st.date_input(
                                    "开始日期",
                                    value=datetime.strptime(selected_cs["start_date"], "%Y-%m-%d"),
                                    key="cs_task_start"
                                )
                            with col_task2:
                                task_duration = st.number_input("工期（天）*", min_value=1, value=1,
                                                                key="cs_task_duration")
                                task_end = task_start + timedelta(days=task_duration - 1)  # 工期=结束-开始+1
                                st.text(f"结束日期（自动计算）：{task_end.strftime('%Y-%m-%d')}")

                            # 依赖设置（支持四种类型）
                            dep_task_options = ["无"] + [f"{t['name']}（T-{t['id'][-4:]}）" for t in
                                                         st.session_state.cs_tasks.values() if
                                                         t["cs_id"] == selected_cs_id]
                            dep_task = st.selectbox("前置任务", dep_task_options, key="cs_dep_task")
                            dep_type = st.selectbox("依赖类型", [
                                "FS（完成→开始）",
                                "SS（开始→开始）",
                                "FF（完成→完成）",
                                "SF（开始→完成）"
                            ], key="cs_dep_type")

                            if st.button("添加任务", key="cs_add_task"):
                                if not task_name:
                                    st.warning("任务名称为必填项")
                                else:
                                    dep_task_id = None
                                    if dep_task != "无":
                                        dep_short_id = dep_task.split("（T-")[1].split("）")[0]
                                        for t_id, t in st.session_state.cs_tasks.items():
                                            if t["id"].endswith(dep_short_id) and t["cs_id"] == selected_cs_id:
                                                dep_task_id = t_id
                                                break

                                    # 转换为相对计划开始的天数（基础日期）
                                    # 转换为相对计划开始的天数（基础日期）
                                    base_date = datetime.strptime(selected_cs["start_date"], "%Y-%m-%d").date()
                                    # 修正这一行：移除 .date()
                                    start_days = (task_start - base_date).days
                                    end_days = start_days + task_duration - 1  # 结束=开始+工期-1
                                    st.session_state.cs_tasks[task_id] = {
                                        "id": task_id,
                                        "cs_id": selected_cs_id,
                                        "name": task_name,
                                        "start_date": task_start.strftime("%Y-%m-%d"),
                                        "end_date": task_end.strftime("%Y-%m-%d"),
                                        "start_days": start_days,  # 相对基础日期的天数
                                        "end_days": end_days,
                                        "duration": task_duration,
                                        "dependencies": [{  # 存储依赖详情（任务ID+类型）
                                            "task_id": dep_task_id,
                                            "type": dep_type
                                        }] if dep_task_id else [],
                                        "successors": [],  # 后置任务ID（自动维护）
                                        "ES": 0, "EF": 0,  # 最早开始/完成
                                        "LS": 0, "LF": 0,  # 最晚开始/完成
                                        "float": 0,  # 总浮动=LS-ES
                                        "is_critical": False
                                    }

                                    # 更新前置任务的后置任务列表
                                    if dep_task_id:
                                        st.session_state.cs_tasks[dep_task_id]["successors"].append(task_id)
                                    st.session_state.cs_plans[selected_cs_id]["tasks"].append(task_id)
                                    st.success(f"任务「{task_name}」已添加（工期：{task_duration}天，依赖：{dep_type}）")
                                    rerun()

                        # 展示任务并计算关键路径
                        if selected_cs["tasks"]:
                            tasks = {tid: st.session_state.cs_tasks[tid] for tid in selected_cs["tasks"]}
                            plan_start_date = datetime.strptime(selected_cs["start_date"], "%Y-%m-%d")


                            # ------------------------------
                            # 核心：四种依赖类型的CPM计算逻辑
                            # ------------------------------
                            def calculate_cpm_with_dependencies(tasks):
                                # 1. 正向计算ES（最早开始）和EF（最早完成）
                                # 按依赖关系排序（确保前置任务先计算）
                                sorted_tasks = []
                                visited = set()

                                def forward_sort(tid):
                                    if tid in visited:
                                        return
                                    visited.add(tid)
                                    # 先处理所有前置依赖任务
                                    for dep in tasks[tid]["dependencies"]:
                                        pred_id = dep["task_id"]
                                        if pred_id in tasks:
                                            forward_sort(pred_id)
                                    sorted_tasks.append(tid)

                                for tid in tasks:
                                    if tid not in visited:
                                        forward_sort(tid)

                                # 计算ES和EF（根据依赖类型动态调整）
                                for tid in sorted_tasks:
                                    task = tasks[tid]
                                    # 初始值：使用任务计划的开始/结束时间
                                    task["ES"] = task["start_days"]
                                    task["EF"] = task["end_days"]

                                    # 根据依赖类型调整ES/EF
                                    for dep in task["dependencies"]:
                                        pred_id = dep["task_id"]
                                        if pred_id not in tasks:
                                            continue
                                        pred = tasks[pred_id]

                                        # 四种依赖类型的正向计算规则
                                        if dep["type"] == "FS（完成→开始）":
                                            # 本任务ES ≥ 前置任务EF（前置完成后才能开始）
                                            task["ES"] = max(task["ES"], pred["EF"])
                                        elif dep["type"] == "SS（开始→开始）":
                                            # 本任务ES ≥ 前置任务ES（前置开始后才能开始）
                                            task["ES"] = max(task["ES"], pred["ES"])
                                        elif dep["type"] == "FF（完成→完成）":
                                            # 本任务EF ≥ 前置任务EF（前置完成后才能完成）
                                            task["EF"] = max(task["EF"], pred["EF"])
                                        elif dep["type"] == "SF（开始→完成）":
                                            # 本任务EF ≥ 前置任务ES（前置开始后才能完成）
                                            task["EF"] = max(task["EF"], pred["ES"])

                                    # 确保EF与ES+工期一致（修正依赖导致的冲突）
                                    task["EF"] = max(task["EF"], task["ES"] + task["duration"] - 1)

                                # 2. 确定项目总工期（所有任务EF的最大值）
                                total_duration = max(task["EF"] for task in tasks.values()) if tasks else 0

                                # 3. 反向计算LF（最晚完成）和LS（最晚开始）
                                # 按依赖关系反向排序（确保后置任务先计算）
                                reversed_tasks = list(reversed(sorted_tasks))

                                for tid in reversed_tasks:
                                    task = tasks[tid]
                                    # 初始值：使用项目总工期或任务计划的结束时间
                                    task["LF"] = total_duration
                                    task["LS"] = task["LF"] - task["duration"] + 1  # LS = LF - 工期 + 1（含首尾）

                                    # 根据依赖类型调整LS/LF（通过后置任务反推）
                                    for succ_id in task["successors"]:
                                        if succ_id not in tasks:
                                            continue
                                        succ = tasks[succ_id]
                                        # 找到后置任务中依赖当前任务的关系
                                        relevant_dep = next((d for d in succ["dependencies"] if d["task_id"] == tid),
                                                            None)
                                        if not relevant_dep:
                                            continue

                                        # 四种依赖类型的反向计算规则
                                        if relevant_dep["type"] == "FS（完成→开始）":
                                            # 前置任务LF ≤ 后置任务LS - 1（本任务需在后置开始前完成）
                                            task["LF"] = min(task["LF"], succ["LS"] - 1)
                                        elif relevant_dep["type"] == "SS（开始→开始）":
                                            # 前置任务LS ≤ 后置任务ES（本任务需在后置开始前开始）
                                            task["LS"] = min(task["LS"], succ["ES"])
                                        elif relevant_dep["type"] == "FF（完成→完成）":
                                            # 前置任务LF ≤ 后置任务LF（本任务需在后置完成前完成）
                                            task["LF"] = min(task["LF"], succ["LF"])
                                        elif relevant_dep["type"] == "SF（开始→完成）":
                                            # 前置任务LS ≤ 后置任务EF（本任务需在后置完成前开始）
                                            task["LS"] = min(task["LS"], succ["EF"])

                                    # 确保LS与LF-工期+1一致（修正依赖导致的冲突）
                                    task["LS"] = min(task["LS"], task["LF"] - task["duration"] + 1)

                                # 4. 计算总浮动时间（关键：总浮动=LS-ES）
                                for task in tasks.values():
                                    task["float"] = task["LS"] - task["ES"]
                                    task["is_critical"] = abs(task["float"]) < 1e-6  # 允许微小误差

                                # 5. 识别关键路径（总浮动=0的任务链）
                                # 找到起点任务（无前置依赖且为关键任务）
                                start_tasks = [tid for tid, t in tasks.items() if
                                               not t["dependencies"] and t["is_critical"]]
                                critical_path = []

                                if start_tasks:
                                    # 递归查找关键路径
                                    def find_critical_chain(current_tid, path):
                                        new_path = path + [current_tid]
                                        # 终点任务（无后置任务）
                                        if not tasks[current_tid]["successors"]:
                                            return [new_path]
                                        # 递归查找关键后置任务
                                        all_paths = []
                                        for succ_id in tasks[current_tid]["successors"]:
                                            if tasks[succ_id]["is_critical"]:
                                                all_paths.extend(find_critical_chain(succ_id, new_path))
                                        return all_paths

                                    # 取最长的关键路径
                                    all_chains = []
                                    for start_tid in start_tasks:
                                        all_chains.extend(find_critical_chain(start_tid, []))
                                    if all_chains:
                                        critical_path = max(all_chains, key=lambda x: len(x))

                                return total_duration, tasks, critical_path


                            # 执行CPM计算（支持四种依赖类型）
                            total_duration, tasks, critical_path = calculate_cpm_with_dependencies(tasks)
                            project_end_date = plan_start_date + timedelta(days=total_duration)

                            # 标记关键路径任务
                            critical_task_ids = set(critical_path)
                            for tid in tasks:
                                tasks[tid]["is_critical"] = tid in critical_task_ids

                            # 任务详情表格（含四种依赖类型）
                            task_df = pd.DataFrame([{
                                "任务ID": f"T-{t['id'][-4:]}",
                                "任务名称": t["name"],
                                "计划开始": t["start_date"],
                                "计划结束": t["end_date"],
                                "工期（天）": t["duration"],
                                "前置依赖": ", ".join([
                                    f"{tasks[dep['task_id']]['name']}（T-{tasks[dep['task_id']]['id'][-4:]}，{dep['type']}）"
                                    for dep in t["dependencies"] if dep["task_id"] in tasks
                                ]) if t["dependencies"] else "无",
                                "最早开始（ES）": (plan_start_date + timedelta(days=t["ES"])).strftime("%Y-%m-%d"),
                                "最早完成（EF）": (plan_start_date + timedelta(days=t["EF"])).strftime("%Y-%m-%d"),
                                "最晚开始（LS）": (plan_start_date + timedelta(days=t["LS"])).strftime("%Y-%m-%d"),
                                "最晚完成（LF）": (plan_start_date + timedelta(days=t["LF"])).strftime("%Y-%m-%d"),
                                "总浮动（天）": round(t["float"], 1),
                                "是否关键任务": "是" if t["is_critical"] else "否"
                            } for t in tasks.values()])
                            st.dataframe(task_df, use_container_width=True)

                            # 显示关键路径
                            if critical_path:
                                critical_chain = [f"T-{tasks[tid]['id'][-4:]} {tasks[tid]['name']}" for tid in
                                                  critical_path]
                                st.success(f"**关键路径**（总浮动=0的任务链）：\n{' → '.join(critical_chain)}")
                            else:
                                st.warning("未找到关键路径，请检查任务依赖是否形成完整链条")


                            # 甘特图（突出关键路径）
                            def generate_gantt_with_dependencies(tasks, critical_path, title):
                                df = []
                                task_list = sorted(tasks.values(), key=lambda x: x["ES"])  # 按最早开始排序
                                critical_ids = set(critical_path)

                                for t in task_list:
                                    is_critical = t["id"] in critical_ids
                                    df.append({
                                        "Task": f"{'🔴' if is_critical else '⚪'} {t['name']} (T-{t['id'][-4:]})",
                                        "Start": datetime.strptime(t["start_date"], "%Y-%m-%d"),
                                        "Finish": datetime.strptime(t["end_date"], "%Y-%m-%d"),
                                        "Type": "关键路径" if is_critical else "非关键路径"
                                    })

                                # 关键路径红色，非关键路径蓝色
                                colors = {"关键路径": "#FF4444", "非关键路径": "#3366FF"}
                                fig = ff.create_gantt(
                                    df,
                                    colors=colors,
                                    index_col="Type",
                                    show_colorbar=False,
                                    title=title,
                                    bar_width=0.6,
                                    showgrid_x=True,
                                    showgrid_y=True
                                )

                                # 绘制关键路径连接线
                                if critical_path and len(critical_path) > 1:
                                    for i in range(len(critical_path) - 1):
                                        curr_tid = critical_path[i]
                                        next_tid = critical_path[i + 1]
                                        curr_t = tasks[curr_tid]
                                        next_t = tasks[next_tid]

                                        # 连接线坐标
                                        curr_y = [idx for idx, t in enumerate(task_list) if t["id"] == curr_tid][0]
                                        next_y = [idx for idx, t in enumerate(task_list) if t["id"] == next_tid][0]
                                        curr_end = datetime.strptime(curr_t["end_date"], "%Y-%m-%d")
                                        next_start = datetime.strptime(next_t["start_date"], "%Y-%m-%d")

                                        # 红色虚线连接关键任务
                                        fig.add_shape(
                                            type="line",
                                            x0=curr_end, y0=curr_y,
                                            x1=next_start, y1=next_y,
                                            line=dict(color="#FF4444", width=2, dash="dash")
                                        )

                                # 标注依赖类型（仅关键路径）
                                for tid in critical_path:
                                    task = tasks[tid]
                                    for dep in task["dependencies"]:
                                        if dep["task_id"] in critical_ids:  # 仅标注关键路径内的依赖
                                            pred_t = tasks[dep["task_id"]]
                                            y_pos = [idx for idx, t in enumerate(task_list) if t["id"] == tid][0]
                                            fig.add_annotation(
                                                x=datetime.strptime(pred_t["end_date"], "%Y-%m-%d"),
                                                y=y_pos,
                                                text=dep["type"],
                                                showarrow=True,
                                                arrowhead=1,
                                                font=dict(size=9, color="#666666")
                                            )

                                fig.update_layout(
                                    height=600,
                                    xaxis_title="日期",
                                    yaxis_title="任务",
                                    xaxis_tickformat="%Y-%m-%d",
                                    plot_bgcolor="white"
                                )
                                return fig


                            # 展示甘特图
                            fig = generate_gantt_with_dependencies(
                                tasks,
                                critical_path,
                                title=f"{selected_proj_name} - 关键路径计划（支持FS/SS/FF/SF依赖）"
                            )
                            st.plotly_chart(fig, use_container_width=True)

                            # 项目关键信息
                            st.info(f"""
                            **项目最短工期**：{total_duration + 1} 天（含首尾日期）  
                            **项目总时间范围**：{selected_cs['start_date']} 至 {project_end_date.strftime('%Y-%m-%d')}  
                            **关键路径任务数**：{len(critical_path)} 个  
                            **关键路径总工期**：{sum(tasks[tid]['duration'] for tid in critical_path)} 天
                            """)

                            # 编辑任务
                            with st.expander("✏️ 编辑任务", expanded=False):
                                edit_options = [""] + [f"{t['name']} (T-{t['id'][-4:]})" for t in tasks.values()]
                                edit_task = st.selectbox("选择任务", edit_options, key="cs_edit_task")
                                if edit_task:
                                    short_id = edit_task.split("(T-")[1].split(")")[0]
                                    task_id = next(tid for tid, t in tasks.items() if tid.endswith(short_id))
                                    task = tasks[task_id]

                                    new_name = st.text_input("任务名称", value=task["name"], key="cs_edit_name")
                                    new_duration = st.number_input("工期（天）", min_value=1, value=task["duration"],
                                                                   key="cs_edit_duration")

                                    if st.button("保存修改", key="cs_save_edit"):
                                        # 重新计算结束日期
                                        start_date = datetime.strptime(task["start_date"], "%Y-%m-%d")
                                        new_end_date = start_date + timedelta(days=new_duration - 1)
                                        base_date = datetime.strptime(selected_cs["start_date"], "%Y-%m-%d").date()

                                        st.session_state.cs_tasks[task_id].update({
                                            "name": new_name,
                                            "duration": new_duration,
                                            "end_date": new_end_date.strftime("%Y-%m-%d"),
                                            "end_days": (new_end_date.date() - base_date).days
                                        })
                                        st.success("任务已更新，关键路径将重新计算")
                                        rerun()

                            # 删除任务
                            with st.expander("🗑️ 删除任务", expanded=False):
                                del_options = [""] + [f"{t['name']} (T-{t['id'][-4:]})" for t in tasks.values()]
                                del_task = st.selectbox("选择任务", del_options, key="cs_del_task")
                                if del_task and st.button("确认删除", type="primary"):
                                    short_id = del_task.split("(T-")[1].split(")")[0]
                                    task_id = next(tid for tid, t in tasks.items() if tid.endswith(short_id))

                                    # 清理依赖关系
                                    for dep in tasks[task_id]["dependencies"]:
                                        pred_id = dep["task_id"]
                                        if pred_id in st.session_state.cs_tasks:
                                            st.session_state.cs_tasks[pred_id]["successors"].remove(task_id)
                                    for succ_id in tasks[task_id]["successors"]:
                                        if succ_id in st.session_state.cs_tasks:
                                            st.session_state.cs_tasks[succ_id]["dependencies"] = [
                                                d for d in st.session_state.cs_tasks[succ_id]["dependencies"]
                                                if d["task_id"] != task_id
                                            ]

                                    # 删除任务
                                    del st.session_state.cs_tasks[task_id]
                                    st.session_state.cs_plans[selected_cs_id]["tasks"].remove(task_id)
                                    st.success("任务已删除，关键路径将重新计算")
                                    rerun()

                            # ------------------------------
                            # 新增：DeepSeek AI对话助手（CPM优化建议）- 内置API Key版本
                            # ------------------------------
                            st.markdown("---")
                            st.subheader("🤖 CPM关键路径AI助手（DeepSeek）")

                            # 安装依赖提示（首次运行）
                            st.markdown("""
                            <div style='font-size:12px;color:#666;margin-bottom:10px'>
                            提示：使用前请先安装依赖 <code>pip install deepseek-sdk</code>
                            </div>
                            """, unsafe_allow_html=True)

                            # ====================== 核心修改：内置你的API Key ======================
                            # 替换为你自己的DeepSeek API Key
                            YOUR_DEEPSEEK_API_KEY = "your_deepseek_api_key_here"  # 这里填写你的真实API Key
                            # =====================================================================

                            # 初始化对话历史
                            if "deepseek_chat_history" not in st.session_state:
                                st.session_state.deepseek_chat_history = []


                            # 生成项目CPM数据摘要（供AI分析）
                            def generate_cpm_summary(tasks, critical_path, total_duration):
                                # 关键路径状态
                                if not critical_path:
                                    cp_status = "未识别到关键路径，可能原因：1) 任务依赖关系不完整 2) 存在循环依赖 3) 所有任务均有浮动时间"
                                elif len(critical_path) < 2:
                                    cp_status = f"关键路径仅包含{len(critical_path)}个任务，未形成完整任务链"
                                else:
                                    cp_status = f"关键路径包含{len(critical_path)}个任务，总工期{sum(tasks[tid]['duration'] for tid in critical_path)}天，完整覆盖项目首尾"

                                # 任务依赖问题
                                dependency_issues = []
                                for tid, t in tasks.items():
                                    # 检查无效依赖
                                    invalid_deps = [dep for dep in t["dependencies"] if dep["task_id"] not in tasks]
                                    if invalid_deps:
                                        dependency_issues.append(
                                            f"任务T-{tid[-4:]} {t['name']}包含无效前置依赖（任务不存在）")  # 修复语法错误 T - {tid[-4:]} → T-{tid[-4:]}
                                    # 检查循环依赖
                                    if tid in [dep["task_id"] for dep in t["dependencies"]]:
                                        dependency_issues.append(
                                            f"任务T-{tid[-4:]} {t['name']}存在自依赖（循环依赖）")  # 修复语法错误

                                # 工期异常
                                duration_issues = [
                                    f"任务T-{tid[-4:]} {t['name']}工期{t['duration']}天，但总浮动时间{round(t['float'], 1)}天（浮动时间异常）"
                                    for tid, t in tasks.items() if abs(t['float']) > 10]  # 修复语法错误

                                # 生成摘要
                                summary = f"""
                            ### 项目CPM分析摘要
                            项目名称：{selected_proj_name}
                            项目总工期：{total_duration + 1}天
                            关键路径状态：{cp_status}

                            #### 潜在问题
                            1. 依赖关系问题：{'; '.join(dependency_issues) if dependency_issues else '无'}
                            2. 工期/浮动时间异常：{'; '.join(duration_issues) if duration_issues else '无'}
                            3. 关键路径连贯性：{'关键路径未从首个任务连贯到最后一个任务' if critical_path and (critical_path[0] not in [tid for tid, t in tasks.items() if not t['dependencies']] or critical_path[-1] not in [tid for tid, t in tasks.items() if not t['successors']]) else '关键路径连贯'}

                            #### 任务数据
                            总计任务数：{len(tasks)}个
                            关键任务数：{len(critical_path)}个
                            非关键任务数：{len(tasks) - len(critical_path)}个
                            """
                                return summary


                            # 对话输入
                            user_question = st.text_area(
                                "向AI提问（可询问CPM优化建议、关键路径问题排查等）",
                                placeholder=f"""示例问题：
                            1. 为什么我的项目识别不到关键路径？
                            2. 如何优化当前关键路径缩短项目工期？
                            3. 任务依赖关系设置错误该如何调整？
                            4. 分析当前CPM数据的潜在问题并给出改进建议""",
                                key="deepseek_question"
                            )

                            # 发送按钮（修改：不再检查用户输入的API Key）
                            if st.button("📤 发送问题", type="primary") and user_question:
                                # 检查内置API Key是否配置
                                if YOUR_DEEPSEEK_API_KEY == "sk-a45adc800fd44dee9ecdaa234dddcb8a" or not YOUR_DEEPSEEK_API_KEY:
                                    st.error("请先在代码中配置你的DeepSeek API Key（替换YOUR_DEEPSEEK_API_KEY变量）")
                                else:
                                    try:
                                        # 导入DeepSeek SDK（确保已安装）
                                        from deepseek import ChatCompletion

                                        # 生成CPM数据摘要
                                        cpm_summary = generate_cpm_summary(tasks, critical_path, total_duration)

                                        # 构建对话消息
                                        messages = [
                                            {
                                                "role": "system",
                                                "content": f"""你是专业的项目管理CPM关键路径分析专家，基于以下项目CPM数据回答用户问题：
                            {cpm_summary}
                            回答要求：
                            1. 针对CPM关键路径识别问题给出具体排查步骤
                            2. 针对依赖关系/工期设置错误给出修正建议
                            3. 针对关键路径不连贯问题给出调整方案
                            4. 语言通俗易懂，给出可落地的具体建议
                            """
                                            },
                                            {"role": "user", "content": user_question}
                                        ]

                                        # 调用DeepSeek API（使用内置API Key）
                                        response = ChatCompletion.create(
                                            api_key=YOUR_DEEPSEEK_API_KEY,  # 使用内置的API Key
                                            model="deepseek-chat",  # 可替换为deepseek-coder等模型
                                            messages=messages,
                                            temperature=0.7,
                                            stream=False
                                        )

                                        # 保存对话历史
                                        st.session_state.deepseek_chat_history.append({
                                            "role": "user",
                                            "content": user_question
                                        })
                                        st.session_state.deepseek_chat_history.append({
                                            "role": "assistant",
                                            "content": response.choices[0].message.content
                                        })

                                    except ImportError:
                                        st.error("未安装DeepSeek SDK，请执行：pip install deepseek-sdk")
                                    except Exception as e:
                                        st.error(f"调用DeepSeek API失败：{str(e)}")
                            elif st.button("📤 发送问题") and not user_question:
                                st.warning("请输入要咨询的问题")

                            # 显示对话历史
                            if st.session_state.deepseek_chat_history:
                                st.markdown("### 对话历史")
                                for msg in st.session_state.deepseek_chat_history:
                                    if msg["role"] == "user":
                                        st.chat_message("user").write(msg["content"])
                                    else:
                                        st.chat_message("assistant").write(msg["content"])

                            # 清空对话历史按钮
                            if st.button("🗑️ 清空对话历史"):
                                st.session_state.deepseek_chat_history = []
                                st.rerun()

                            # 修复原有的逻辑错误（移除多余的elif/else）
                            if not critical_path and not tasks:
                                st.info("暂无CS计划，请点击「新建CS计划」")
        # 其他计划编制子模块（保持占位）
        # ------------------------------
        # 2.4 计划编制（BS，平衡计分卡）
        # 核心功能：从4个维度设定项目指标，关联项目/人员，跟踪目标达成率，可视化分析
        # ------------------------------
        with plan_sub_tab[3]:
            st.subheader("计划编制（BS，平衡计分卡）")
            st.write("""
            平衡计分卡（Balanced Scorecard）：从4个核心维度量化项目目标，确保战略落地：
            - 📊 财务维度：项目经济效益（如成本控制、收益达成）
            - 👥 客户维度：利益相关方满意度（如需求满足率、反馈评分）
            - 🔧 内部流程：项目执行效率（如任务完成率、质量合格率）
            - 📈 学习与成长：团队能力提升（如技能掌握率、经验沉淀）
            """)


            # 补充：计算整体达成率的工具函数（必须放在使用前）
            def calculate_bs_overall_rate(project_id):
                """计算项目BS指标的整体加权达成率"""
                project_metrics = [m for m in st.session_state.bs_metrics.values() if m["project_id"] == project_id]
                if not project_metrics:
                    return 0.0
                total_weighted_completion = 0.0
                total_weight = 0.0
                for metric in project_metrics:
                    completion_rate = (metric["actual"] / metric["target"]) * 100 if metric["target"] != 0 else 0
                    total_weighted_completion += completion_rate * metric["weight"]
                    total_weight += metric["weight"]
                return total_weighted_completion / total_weight if total_weight != 0 else 0.0


            # 工具函数（确保依赖函数存在）
            def generate_unique_id(prefix="BS_METRIC"):
                import uuid
                return f"{prefix}_{uuid.uuid4().hex[:8]}"


            def get_current_date():
                from datetime import datetime
                return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


            def get_employee_id(emp_name):
                """根据员工姓名获取ID"""
                for emp_id, emp in st.session_state.employees.items():
                    if emp["name"] == emp_name:
                        return emp_id
                return ""


            def rerun():
                try:
                    st.rerun()
                except AttributeError:
                    st.experimental_rerun()


            # 初始化BS指标数据结构
            if "bs_metrics" not in st.session_state:
                st.session_state.bs_metrics = {}

            # 选择项目（与前面基础数据关联）
            if not st.session_state.projects:
                st.warning("请先在「基础数据」创建项目")
            else:
                # 项目选择下拉框（关联已创建的项目）
                project_options = {proj["name"]: proj["id"] for proj in st.session_state.projects.values()}
                selected_proj_name = st.selectbox("选择项目", list(project_options.keys()), key="bs_proj_select")
                selected_proj_id = project_options[selected_proj_name]
                selected_proj = st.session_state.projects[selected_proj_id]

                # 项目基本信息展示（折叠面板）
                with st.expander("当前项目信息", expanded=False):
                    col_proj1, col_proj2, col_proj3 = st.columns(3)
                    with col_proj1:
                        st.write(f"**项目ID**：{selected_proj['id']}")
                        st.write(f"**项目经理**：{selected_proj['manager']}")
                    with col_proj2:
                        st.write(f"**项目状态**：{selected_proj['status']}")
                        st.write(f"**创建日期**：{selected_proj['create_date']}")
                    with col_proj3:
                        metric_count = len(
                            [m for m in st.session_state.bs_metrics.values() if m["project_id"] == selected_proj_id])
                        st.write(f"**关联指标数**：{metric_count}")


                        # 补充calculate_bs_overall_rate函数（避免未定义报错）
                        def calculate_bs_overall_rate(proj_id):
                            metrics = [m for m in st.session_state.bs_metrics.values() if m["project_id"] == proj_id]
                            if not metrics:
                                return 0.0
                            total_weight = sum(m["weight"] for m in metrics)
                            if total_weight == 0:
                                return 0.0
                            weighted_rate = sum(
                                (m["actual"] / m["target"] * 100 if m["target"] != 0 else 0) * m["weight"] for m in
                                metrics)
                            return weighted_rate / total_weight


                        st.write(f"**整体达成率**：{calculate_bs_overall_rate(selected_proj_id):.1f}%")

                # ------------------------------
                # 1. 新增BS指标
                # ------------------------------
                st.markdown("---")
                st.subheader("➕ 新增指标")
                with st.form(key="bs_add_metric_form"):
                    col1, col2 = st.columns(2)

                    # 基础信息
                    with col1:
                        # 维度选择（固定4个核心维度）
                        dimension = st.selectbox(
                            "指标维度*",
                            ["财务维度", "客户维度", "内部流程", "学习与成长"],
                            key="bs_dimension"
                        )
                        # 指标名称（必填）
                        metric_name = st.text_input("指标名称*", placeholder="如：成本控制率、客户满意度",
                                                    key="bs_metric_name")
                        # 指标类型（量化/质化）
                        metric_type = st.selectbox(
                            "指标类型*",
                            ["量化指标（可计算数值）", "质化指标（等级评分）"],
                            key="bs_metric_type"
                        )

                    with col2:
                        # 目标值（必填）
                        target_value = st.number_input(
                            "目标值*",
                            min_value=0.0,
                            step=0.1,
                            placeholder="如：95（%）、8（分）",
                            key="bs_target_value"
                        )
                        # 权重（必填，4个维度权重总和建议为100%）
                        weight = st.number_input(
                            "指标权重（%）*",
                            min_value=1,
                            max_value=100,
                            value=20,
                            key="bs_weight"
                        )
                        # 责任人（关联已创建的人员）
                        responsible = st.selectbox(
                            "责任人*",
                            ["请选择"] + [emp["name"] for emp in st.session_state.employees.values()],
                            key="bs_responsible"
                        )

                    # 补充信息
                    st.markdown("---")
                    col3, col4 = st.columns(2)
                    with col3:
                        # 测量单位
                        unit = st.text_input("测量单位", placeholder="如：%、分、个、元", key="bs_unit")
                        # 指标描述
                        description = st.text_area("指标描述", placeholder="说明指标的计算方式、统计周期等",
                                                   key="bs_description")
                    with col4:
                        # 统计周期
                        cycle = st.selectbox(
                            "统计周期",
                            ["项目全程", "月度", "季度", "里程碑节点"],
                            key="bs_cycle"
                        )
                        # 初始实际值（可后续修改）
                        actual_value = st.number_input(
                            "当前实际值",
                            min_value=0.0,
                            step=0.1,
                            value=0.0,
                            key="bs_actual_value"
                        )

                    # 提交按钮
                    submit_btn = st.form_submit_button("保存指标", type="primary")
                    if submit_btn:
                        # 表单校验
                        if not metric_name.strip():
                            st.warning("指标名称为必填项")
                        elif target_value <= 0:
                            st.warning("目标值必须大于0")
                        elif responsible == "请选择":
                            st.warning("请选择责任人")
                        else:
                            # 生成唯一指标ID
                            metric_id = generate_unique_id("BS_METRIC")
                            # 获取责任人ID（关联人员数据）
                            responsible_id = get_employee_id(responsible)
                            # 存储指标到会话状态
                            st.session_state.bs_metrics[metric_id] = {
                                "id": metric_id,
                                "project_id": selected_proj_id,
                                "project_name": selected_proj_name,
                                "dimension": dimension,
                                "name": metric_name.strip(),
                                "type": metric_type,
                                "target": target_value,
                                "actual": actual_value,
                                "unit": unit.strip(),
                                "weight": weight,
                                "responsible": responsible,
                                "responsible_id": responsible_id,
                                "cycle": cycle,
                                "description": description.strip(),
                                "create_date": get_current_date(),
                                "last_update_date": get_current_date()
                            }
                            st.success(f"✅ 指标「{metric_name}」已创建成功！")
                            rerun()

                # ------------------------------
                # 2. 指标列表与编辑
                # ------------------------------
                st.markdown("---")
                st.subheader("📋 指标跟踪列表")

                # 筛选当前项目的所有BS指标
                project_metrics = [m for m in st.session_state.bs_metrics.values() if
                                   m["project_id"] == selected_proj_id]

                if project_metrics:
                    # 准备表格数据（拆分数值和单位，避免类型混合）
                    metric_table = []
                    for idx, metric in enumerate(project_metrics, 1):
                        # 计算达成率（避免除以0）
                        completion_rate = (metric["actual"] / metric["target"]) * 100 if metric["target"] != 0 else 0
                        # 状态判断
                        if completion_rate >= 100:
                            status = "✅ 已达成"
                        elif completion_rate >= 80:
                            status = "⚠️ 接近目标"
                        else:
                            status = "❌ 待提升"

                        metric_table.append({
                            "序号": idx,
                            "维度": metric["dimension"],
                            "指标名称": metric["name"],
                            "指标类型": metric["type"].split("（")[0],
                            "目标值": metric["target"],  # 纯数值，不拼接单位
                            "目标单位": metric["unit"],  # 单独存储单位
                            "实际值": metric["actual"],  # 纯数值，用于编辑
                            "达成率": completion_rate,
                            "权重": metric["weight"],
                            "责任人": metric["responsible"],
                            "统计周期": metric["cycle"],
                            "状态": status,
                            "最后更新": metric["last_update_date"],
                            "操作": metric["id"],  # 用于编辑/删除的隐藏ID
                            "显示目标值": f"{metric['target']} {metric['unit']}" if metric["unit"] else metric[
                                "target"],
                            "显示实际值": f"{metric['actual']} {metric['unit']}" if metric["unit"] else metric["actual"]
                        })

                    # 展示指标表格
                    df_metrics = pd.DataFrame(metric_table)
                    edited_df = st.data_editor(
                        # 只展示需要的列，实际值用纯数值列编辑
                        df_metrics[["序号", "维度", "指标名称", "指标类型", "显示目标值", "实际值", "达成率",
                                    "权重", "责任人", "统计周期", "状态", "最后更新"]],
                        use_container_width=True,
                        num_rows="dynamic",
                        column_config={
                            "序号": st.column_config.NumberColumn(width="small", disabled=True),
                            "维度": st.column_config.TextColumn(width="small", disabled=True),
                            "指标名称": st.column_config.TextColumn(width="medium", disabled=True),
                            "指标类型": st.column_config.TextColumn(width="small", disabled=True),
                            "显示目标值": st.column_config.TextColumn("目标值", width="small", disabled=True),
                            "实际值": st.column_config.NumberColumn(width="small", format="%.1f"),  # 核心修复：数值类型匹配
                            "达成率": st.column_config.NumberColumn(width="small", format="%.1f%%", disabled=True),
                            "权重": st.column_config.NumberColumn(width="small", disabled=True),
                            "责任人": st.column_config.TextColumn(width="small", disabled=True),
                            "统计周期": st.column_config.TextColumn(width="small", disabled=True),
                            "状态": st.column_config.TextColumn(width="small", disabled=True),
                            "最后更新": st.column_config.TextColumn(width="small", disabled=True)
                        },
                        key="bs_metric_editor"
                    )

                    # 保存表格编辑（仅实际值修改）
                    if st.button("保存实际值更新", type="secondary"):
                        # 建立指标名称→ID的映射
                        name_to_id = {m["name"]: m["id"] for m in project_metrics}

                        for _, row in edited_df.iterrows():
                            metric_id = name_to_id.get(row["指标名称"])
                            if not metric_id:
                                continue

                            # 直接获取数值（无需处理字符串，因为用了NumberColumn）
                            actual_value = row["实际值"]
                            if pd.isna(actual_value):
                                actual_value = 0.0

                            # 更新指标数据
                            st.session_state.bs_metrics[metric_id].update({
                                "actual": float(actual_value),
                                "last_update_date": get_current_date()
                            })

                        st.success("✅ 实际值已更新！")
                        rerun()
                    # 批量删除指标（折叠面板）
                    with st.expander("🗑️ 批量删除指标", expanded=False):
                        metrics_to_delete = st.multiselect(
                            "选择要删除的指标",
                            [f"{m['name']}（{m['dimension']}）" for m in project_metrics],
                            key="bs_metrics_delete"
                        )
                        if metrics_to_delete and st.button("确认删除", type="primary"):
                            # 提取要删除的指标ID
                            delete_ids = [name_to_id[m.split("（")[0]] for m in metrics_to_delete]
                            for metric_id in delete_ids:
                                if metric_id in st.session_state.bs_metrics:
                                    del st.session_state.bs_metrics[metric_id]
                            st.success(f"已删除 {len(delete_ids)} 个指标")
                            rerun()

                else:
                    st.info("当前项目暂无BS指标，请点击「新增指标」创建")

                # ------------------------------
                # 3. 指标可视化分析
                # ------------------------------
                st.markdown("---")
                st.subheader("📊 指标达成分析")

                if project_metrics:
                    # 计算各维度的核心数据
                    dimension_data = defaultdict(dict)
                    for metric in project_metrics:
                        dim = metric["dimension"]
                        completion_rate = (metric["actual"] / metric["target"]) * 100 if metric["target"] != 0 else 0

                        # 维度汇总：权重加权平均达成率
                        if dim not in dimension_data:
                            dimension_data[dim] = {"total_weight": 0, "weighted_completion": 0, "metric_count": 0}
                        dimension_data[dim]["total_weight"] += metric["weight"]
                        dimension_data[dim]["weighted_completion"] += completion_rate * metric["weight"]
                        dimension_data[dim]["metric_count"] += 1

                    # 计算各维度加权达成率
                    dim_names = []
                    dim_completion = []
                    dim_weights = []
                    for dim, data in dimension_data.items():
                        dim_names.append(dim)
                        # 加权平均达成率 = 加权总达成率 / 总权重
                        weighted_rate = data["weighted_completion"] / data["total_weight"] if data[
                                                                                                  "total_weight"] != 0 else 0
                        dim_completion.append(weighted_rate)
                        dim_weights.append(data["total_weight"])

                    # 图表1：各维度达成率柱状图
                    fig1 = px.bar(
                        x=dim_names,
                        y=dim_completion,
                        title=f"{selected_proj_name} - 各维度加权达成率",
                        labels={"x": "维度", "y": "加权达成率（%）"},
                        color=dim_names,
                        color_discrete_sequence=["#1E88E5", "#4CAF50", "#FFC107", "#FF5722"],
                        text=[f"{rate:.1f}%" for rate in dim_completion]
                    )
                    fig1.update_layout(
                        yaxis_range=[0, 120],  # y轴范围0-120%，留有余地
                        plot_bgcolor="white",
                        showlegend=False
                    )
                    st.plotly_chart(fig1, use_container_width=True)

                    # 图表2：各维度权重饼图
                    fig2 = px.pie(
                        values=dim_weights,
                        names=dim_names,
                        title=f"{selected_proj_name} - 各维度权重分布",
                        hole=0.3  # 环形图样式
                    )
                    fig2.update_layout(
                        plot_bgcolor="white",
                        legend_title_text="维度"
                    )
                    st.plotly_chart(fig2, use_container_width=True)

                    # 图表3：指标达成率详情（横向柱状图）
                    metric_names = [m["name"] for m in project_metrics]
                    metric_completion = [(m["actual"] / m["target"]) * 100 if m["target"] != 0 else 0 for m in
                                         project_metrics]
                    metric_dimensions = [m["dimension"] for m in project_metrics]

                    fig3 = px.bar(
                        y=metric_names,
                        x=metric_completion,
                        title=f"{selected_proj_name} - 各指标达成率详情",
                        labels={"x": "达成率（%）", "y": "指标名称"},
                        color=metric_dimensions,
                        color_discrete_sequence=["#1E88E5", "#4CAF50", "#FFC107", "#FF5722"],
                        orientation="h"
                    )
                    fig3.update_layout(
                        xaxis_range=[0, 120],
                        plot_bgcolor="white",
                        legend_title_text="维度"
                    )
                    # 添加目标线（100%达成）
                    fig3.add_vline(
                        x=100,
                        line_dash="dash",
                        line_color="red",
                        annotation_text="目标线（100%）",
                        annotation_position="top"
                    )
                    st.plotly_chart(fig3, use_container_width=True)

                    # 整体达成率汇总卡片（修复col_card1未定义问题）
                    st.markdown("---")
                    st.subheader("🎯 整体达成汇总")
                    col_card1, col_card2 = st.columns(2)  # 定义2列容器
                    overall_completion = calculate_bs_overall_rate(selected_proj_id)

                    with col_card1:
                        # 整体达成率卡片
                        st.markdown(f"""
                        <div style='padding:20px;background-color:#f0f8fb;border-radius:10px;text-align:center'>
                            <h4 style='margin:0;color:#2d3748'>项目整体加权达成率</h4>
                            <p style='margin:10px 0;font-size:32px;font-weight:bold;color:#4299e1'>{overall_completion:.1f}%</p>
                            <p style='margin:0;color:#718096'>所有维度指标加权平均</p>
                        </div>
                        """, unsafe_allow_html=True)

                    with col_card2:
                        # 状态判断卡片
                        if overall_completion >= 100:
                            status_text = "🎉 目标达成"
                            status_color = "#48bb78"
                            suggest = "保持当前节奏，巩固成果"
                        elif overall_completion >= 80:
                            status_text = "⚠️ 接近目标"
                            status_color = "#ed8936"
                            suggest = "重点提升低达成率维度，确保整体达标"
                        else:
                            status_text = "❌ 待提升"
                            status_color = "#e53e3e"
                            suggest = "立即分析低达成率指标，制定改进措施"

                        st.markdown(f"""
                        <div style='padding:20px;background-color:#fdf2f8;border-radius:10px;text-align:center'>
                            <h4 style='margin:0;color:#2d3748'>整体状态</h4>
                            <p style='margin:10px 0;font-size:32px;font-weight:bold;color:{status_color}'>{status_text}</p>
                            <p style='margin:0;color:#718096'>{suggest}</p>
                        </div>
                        """, unsafe_allow_html=True)

                        # 导出分析报告
                        if st.button("📥 导出分析报告", type="secondary"):
                            # 准备导出数据
                            export_data = []
                            for metric in project_metrics:
                                completion_rate = (metric["actual"] / metric["target"]) * 100 if metric[
                                                                                                     "target"] != 0 else 0
                                export_data.append({
                                    "项目名称": selected_proj_name,
                                    "维度": metric["dimension"],
                                    "指标名称": metric["name"],
                                    "指标类型": metric["type"],
                                    "目标值": f"{metric['target']} {metric['unit']}" if metric["unit"] else metric[
                                        "target"],
                                    "实际值": f"{metric['actual']} {metric['unit']}" if metric["unit"] else metric[
                                        "actual"],
                                    "达成率(%)": f"{completion_rate:.1f}",
                                    "权重(%)": metric["weight"],
                                    "责任人": metric["responsible"],
                                    "统计周期": metric["cycle"],
                                    "最后更新时间": metric["last_update_date"]
                                })

                            # 导出Excel
                            df_export = pd.DataFrame(export_data)
                            buffer = BytesIO()
                            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                                df_export.to_excel(writer, index=False, sheet_name='BS指标分析')
                                # 新增汇总表
                                summary_data = {
                                    "项目名称": [selected_proj_name],
                                    "整体加权达成率(%)": [f"{overall_completion:.1f}"],
                                    "指标总数": [len(project_metrics)],
                                    "导出时间": [get_current_date()]
                                }
                                pd.DataFrame(summary_data).to_excel(writer, index=False, sheet_name='汇总信息')
                            buffer.seek(0)

                            st.download_button(
                                label="下载Excel报告",
                                data=buffer,
                                file_name=f"{selected_proj_name}_BS平衡计分卡分析报告_{get_current_date().split(' ')[0]}.xlsx",
                                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                            )
                else:
                    st.info("暂无指标数据，无法生成分析图表，请先创建BS指标")
        with plan_sub_tab[4]:
            st.subheader("审批记录")

            # ========== 核心数据初始化 ==========
            # 初始化计划数据（防止未定义）
            if "plans" not in st.session_state:
                st.session_state.plans = {}  # 格式: {plan_id: {id, name, project_id, status, ...}}
            # 初始化审批记录数据结构
            if "approval_records" not in st.session_state:
                st.session_state.approval_records = {}  # 格式: {record_id: {审批记录详情}}
            # 确保选中项目ID/名称存在（防止未定义）
            if "selected_proj_id" not in st.session_state:
                st.session_state.selected_proj_id = ""
            if "selected_proj_name" not in st.session_state:
                st.session_state.selected_proj_name = ""

            selected_proj_id = st.session_state.selected_proj_id
            selected_proj_name = st.session_state.selected_proj_name

            # ========== 计划选择逻辑 ==========
            # 获取当前项目的所有计划
            project_plans = [p for p in st.session_state.plans.values() if p.get("project_id") == selected_proj_id]

            if not project_plans:
                st.warning("当前项目暂无计划，请先在「计划编制」中创建计划")
            else:
                # 选择需要查看审批记录的计划
                plan_options = {p["name"]: p["id"] for p in project_plans}
                selected_plan_name = st.selectbox("选择计划", list(plan_options.keys()), key="approval_plan_select")
                selected_plan_id = plan_options[selected_plan_name]

                # 筛选该计划的所有审批记录
                plan_approvals = [
                    rec for rec in st.session_state.approval_records.values()
                    if rec.get("plan_id") == selected_plan_id
                ]
                # 按时间倒序排列（最新的在前面）
                plan_approvals.sort(key=lambda x: x.get("approval_time", ""), reverse=True)

                # ========== 审批状态概览 ==========
                current_approval_status = "未提交审批"
                if plan_approvals:
                    current_approval_status = plan_approvals[0].get("status", "未提交审批")

                status_color_map = {
                    "未提交审批": "gray",
                    "审批中": "orange",
                    "已批准": "green",
                    "已驳回": "red"
                }
                st.markdown(
                    f"**当前审批状态**: <span style='color:{status_color_map[current_approval_status]}'>{current_approval_status}</span>",
                    unsafe_allow_html=True
                )

                # ========== 审批操作区 ==========
                col_approve1, col_approve2, col_approve3 = st.columns(3)

                # 提交审批按钮
                with col_approve1:
                    if current_approval_status in ["未提交审批", "已驳回"]:
                        if st.button("提交审批", type="primary", key="submit_approval"):
                            # 生成唯一ID（兼容原有generate_unique_id函数）
                            def generate_unique_id(prefix="APPROVAL"):
                                import uuid
                                return f"{prefix}_{uuid.uuid4().hex[:8]}"


                            # 获取当前时间（兼容原有get_current_date函数）
                            def get_current_date():
                                from datetime import datetime
                                return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


                            # 确保用户名存在
                            if "username" not in st.session_state:
                                st.session_state.username = "未知用户"

                            # 创建新的审批记录（提交状态）
                            record_id = generate_unique_id("APPROVAL")
                            st.session_state.approval_records[record_id] = {
                                "id": record_id,
                                "plan_id": selected_plan_id,
                                "plan_name": selected_plan_name,
                                "project_id": selected_proj_id,
                                "project_name": selected_proj_name,
                                "submitter": st.session_state.username,  # 提交人（当前登录用户）
                                "submit_time": get_current_date(),
                                "approval_time": None,
                                "approver": None,
                                "status": "审批中",
                                "comment": None
                            }
                            st.success("计划已提交审批！")


                            # 页面刷新（兼容原有rerun函数）
                            def rerun():
                                try:
                                    st.rerun()
                                except AttributeError:
                                    st.experimental_rerun()


                            rerun()

                # 审批人操作区（仅管理员可见）
                if st.session_state.get("user_type") == "管理员":
                    with col_approve2:
                        if current_approval_status == "审批中":
                            if st.button("批准", type="primary", key="approve_plan"):
                                # 更新最新审批记录状态
                                latest_record = plan_approvals[0]
                                st.session_state.approval_records[latest_record["id"]].update({
                                    "status": "已批准",
                                    "approver": st.session_state.username,
                                    "approval_time": get_current_date(),
                                    "comment": "审批通过"
                                })
                                # 同步更新计划状态
                                st.session_state.plans[selected_plan_id]["status"] = "已批准"
                                st.success("已批准该计划！")
                                rerun()
                    with col_approve3:
                        if current_approval_status == "审批中":
                            with st.form(key="reject_form"):
                                reject_comment = st.text_area("驳回原因", placeholder="请输入驳回原因...",
                                                              key="reject_comment")
                                if st.form_submit_button("驳回", type="secondary"):
                                    if not reject_comment.strip():
                                        st.warning("请输入驳回原因")
                                    else:
                                        # 更新最新审批记录状态
                                        latest_record = plan_approvals[0]
                                        st.session_state.approval_records[latest_record["id"]].update({
                                            "status": "已驳回",
                                            "approver": st.session_state.username,
                                            "approval_time": get_current_date(),
                                            "comment": reject_comment.strip()
                                        })
                                        st.success("已驳回该计划！")
                                        rerun()

                # ========== 审批记录列表 ==========
                st.markdown("---")
                st.subheader("审批历史记录")

                if plan_approvals:
                    import pandas as pd

                    # 准备表格数据
                    approval_table = []
                    for idx, record in enumerate(plan_approvals, 1):
                        approval_table.append({
                            "序号": idx,
                            "提交人": record.get("submitter", "未知"),
                            "提交时间": record.get("submit_time", "未知"),
                            "审批人": record.get("approver") or "待审批",
                            "审批时间": record.get("approval_time") or "待审批",
                            "状态": record.get("status", "未知"),
                            "审批意见": record.get("comment") or "无"
                        })

                    # 展示表格
                    df_approvals = pd.DataFrame(approval_table)
                    st.data_editor(
                        df_approvals,
                        use_container_width=True,
                        disabled=True,  # 审批记录只读
                        column_config={
                            "序号": st.column_config.NumberColumn(width="small"),
                            "提交人": st.column_config.TextColumn(width="small"),
                            "提交时间": st.column_config.TextColumn(width="medium"),
                            "审批人": st.column_config.TextColumn(width="small"),
                            "审批时间": st.column_config.TextColumn(width="medium"),
                            "状态": st.column_config.TextColumn(
                                width="small",
                                # 根据状态显示不同颜色
                                formatter=lambda x: f"<span style='color:{status_color_map.get(x, 'black')}'>{x}</span>"
                            ),
                            "审批意见": st.column_config.TextColumn(width="large")
                        }
                    )
                else:
                    st.info("该计划暂无审批记录")

        # ========== 回收记录 Tab ==========
        with plan_sub_tab[5]:
            st.subheader("回收记录")

            # ========== 数据初始化 ==========
            if "recovery_records" not in st.session_state:
                st.session_state.recovery_records = {}  # 格式: {record_id: {回收记录详情}}
            if "employees" not in st.session_state:
                st.session_state.employees = {}  # 初始化员工数据（防止未定义）

            selected_proj_id = st.session_state.get("selected_proj_id", "")
            selected_proj_name = st.session_state.get("selected_proj_name", "")

            # ========== 计划选择逻辑 ==========
            project_plans = [p for p in st.session_state.plans.values() if p.get("project_id") == selected_proj_id]
            if not project_plans:
                st.warning("当前项目暂无计划，请先在「计划编制」中创建计划")
            else:
                # 选择需要查看回收记录的计划
                plan_options = {p["name"]: p["id"] for p in project_plans}
                selected_plan_name = st.selectbox("选择计划", list(plan_options.keys()), key="recovery_plan_select")
                selected_plan_id = plan_options[selected_plan_name]

                # 筛选该计划的所有回收记录
                plan_recoveries = [
                    rec for rec in st.session_state.recovery_records.values()
                    if rec.get("plan_id") == selected_plan_id
                ]
                # 按时间倒序排列
                plan_recoveries.sort(key=lambda x: x.get("recovery_time", ""), reverse=True)

                # ========== 新增回收记录 ==========
                st.markdown("---")
                st.subheader("➕ 记录回收结果")
                with st.form(key="add_recovery_form"):
                    col1, col2 = st.columns(2)
                    with col1:
                        from datetime import datetime

                        recovery_date = st.date_input("回收日期", value=datetime.now(), key="recovery_date")
                        # 员工列表兼容（无员工时显示默认值）
                        employee_list = [emp["name"] for emp in
                                         st.session_state.employees.values()] if st.session_state.employees else [
                            "默认回收人"]
                        recovery_person = st.selectbox(
                            "执行回收人",
                            employee_list,
                            key="recovery_person"
                        )
                    with col2:
                        recovery_type = st.selectbox(
                            "回收类型",
                            ["计划调整回收", "阶段成果回收", "资源回收", "文档回收", "其他"],
                            key="recovery_type"
                        )
                        completion_rate = st.slider(
                            "回收完成率（%）",
                            0, 100, 100, key="recovery_completion"
                        )

                    recovery_details = st.text_area(
                        "回收详情",
                        placeholder="请描述回收的具体内容、遇到的问题、处理结果等...",
                        key="recovery_details"
                    )

                    submit_recovery = st.form_submit_button("保存回收记录", type="primary")
                    if submit_recovery:
                        if not recovery_details.strip():
                            st.warning("请填写回收详情")
                        else:
                            # 工具函数定义（兼容）
                            def generate_unique_id(prefix="RECOVERY"):
                                import uuid
                                return f"{prefix}_{uuid.uuid4().hex[:8]}"


                            def get_current_date():
                                from datetime import datetime
                                return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


                            record_id = generate_unique_id("RECOVERY")
                            st.session_state.recovery_records[record_id] = {
                                "id": record_id,
                                "plan_id": selected_plan_id,
                                "plan_name": selected_plan_name,
                                "project_id": selected_proj_id,
                                "project_name": selected_proj_name,
                                "recovery_date": recovery_date.strftime("%Y-%m-%d"),
                                "recovery_person": recovery_person,
                                "recovery_type": recovery_type,
                                "completion_rate": completion_rate,
                                "details": recovery_details.strip(),
                                "recovery_time": get_current_date()
                            }
                            st.success("回收记录已保存！")


                            # 页面刷新
                            def rerun():
                                try:
                                    st.rerun()
                                except AttributeError:
                                    st.experimental_rerun()


                            rerun()

                # ========== 回收记录列表 ==========
                st.markdown("---")
                st.subheader("📋 回收历史记录")

                if plan_recoveries:
                    import pandas as pd

                    # 准备表格数据
                    recovery_table = []
                    for idx, record in enumerate(plan_recoveries, 1):
                        recovery_table.append({
                            "序号": idx,
                            "回收日期": record.get("recovery_date", "未知"),
                            "回收类型": record.get("recovery_type", "未知"),
                            "执行回收人": record.get("recovery_person", "未知"),
                            "完成率": f"{record.get('completion_rate', 0)}%",
                            "记录时间": record.get("recovery_time", "未知"),
                            "回收详情": record.get("details", "无")
                        })

                    # 展示表格
                    df_recoveries = pd.DataFrame(recovery_table)
                    st.data_editor(
                        df_recoveries,
                        use_container_width=True,
                        disabled=True,
                        column_config={
                            "序号": st.column_config.NumberColumn(width="small"),
                            "回收日期": st.column_config.TextColumn(width="small"),
                            "回收类型": st.column_config.TextColumn(width="small"),
                            "执行回收人": st.column_config.TextColumn(width="small"),
                            "完成率": st.column_config.ProgressColumn(
                                "完成率",
                                width="small",
                                min_value=0,
                                max_value=100,
                                format="%d%%"
                            ),
                            "记录时间": st.column_config.TextColumn(width="medium"),
                            "回收详情": st.column_config.TextColumn(width="large")
                        }
                    )

                    # 导出功能（兼容原有export_to_excel函数）
                    if st.button("导出回收记录", type="secondary"):
                        def export_to_excel(df, filename):
                            import pandas as pd
                            import io
                            buffer = io.BytesIO()
                            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                                df.to_excel(writer, index=False, sheet_name='回收记录')
                            buffer.seek(0)
                            st.download_button(
                                label="下载Excel文件",
                                data=buffer,
                                file_name=f"{filename}.xlsx",
                                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                            )


                        export_df = df_recoveries.copy()
                        export_to_excel(export_df, f"{selected_plan_name}_回收记录_{get_current_date().split(' ')[0]}")
                else:
                    st.info("该计划暂无回收记录")

        # ========== 统筹计划 Tab ==========
        with plan_sub_tab[6]:
            st.subheader("统筹计划")

            # ========== 数据初始化 ==========
            if "coordination_plans" not in st.session_state:
                st.session_state.coordination_plans = {}  # 格式: {plan_id: {统筹计划详情}}
            if "coord_logs" not in st.session_state:
                st.session_state.coord_logs = {}  # 统筹执行日志
            if "projects" not in st.session_state:
                st.session_state.projects = {}  # 初始化项目数据

            selected_proj_id = st.session_state.get("selected_proj_id", "")
            selected_proj_name = st.session_state.get("selected_proj_name", "")

            # ========== 新增统筹计划 ==========
            st.markdown("---")
            st.subheader("➕ 新增统筹计划")
            with st.form(key="add_coordination_form"):
                coord_name = st.text_input("统筹计划名称*", placeholder="如：Q3多项目资源协调计划", key="coord_name")

                col1, col2 = st.columns(2)
                with col1:
                    from datetime import datetime

                    start_date = st.date_input("开始日期*", key="coord_start_date")
                    end_date = st.date_input("结束日期*", key="coord_end_date")
                with col2:
                    coord_type = st.selectbox(
                        "统筹类型*",
                        ["资源协调", "进度协调", "成本协调", "风险协调", "多维度综合协调"],
                        key="coord_type"
                    )
                    # 员工列表兼容
                    employee_list = [emp["name"] for emp in
                                     st.session_state.employees.values()] if st.session_state.employees else [
                        "默认负责人"]
                    responsible_person = st.selectbox(
                        "负责人*",
                        employee_list,
                        key="coord_responsible"
                    )

                # 关联项目（可多选）
                project_list = [p["name"] for p in st.session_state.projects.values() if
                                p.get("id") != selected_proj_id]
                related_projects = st.multiselect(
                    "关联项目",
                    project_list,
                    key="coord_related_projects"
                )
                # 自动包含当前项目（兼容selected_proj_name）
                if selected_proj_name:
                    related_projects = [selected_proj_name] + related_projects
                else:
                    related_projects = project_list[:1] if project_list else ["未选择项目"]

                coord_objective = st.text_area(
                    "统筹目标*",
                    placeholder="说明本次统筹需要解决的问题和达成的目标...",
                    key="coord_objective"
                )
                coord_strategy = st.text_area(
                    "统筹策略",
                    placeholder="说明将采取哪些措施进行统筹协调...",
                    key="coord_strategy"
                )

                submit_coord = st.form_submit_button("创建统筹计划", type="primary")
                if submit_coord:
                    if not coord_name.strip():
                        st.warning("请填写统筹计划名称")
                    elif start_date > end_date:
                        st.warning("结束日期不能早于开始日期")
                    elif not coord_objective.strip():
                        st.warning("请填写统筹目标")
                    else:
                        # 工具函数
                        def generate_unique_id(prefix="COORDINATION"):
                            import uuid
                            return f"{prefix}_{uuid.uuid4().hex[:8]}"


                        def get_current_date():
                            from datetime import datetime
                            return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


                        plan_id = generate_unique_id("COORDINATION")
                        st.session_state.coordination_plans[plan_id] = {
                            "id": plan_id,
                            "name": coord_name.strip(),
                            "project_id": selected_proj_id,
                            "project_name": selected_proj_name,
                            "related_projects": related_projects,
                            "start_date": start_date.strftime("%Y-%m-%d"),
                            "end_date": end_date.strftime("%Y-%m-%d"),
                            "type": coord_type,
                            "responsible": responsible_person,
                            "objective": coord_objective.strip(),
                            "strategy": coord_strategy.strip(),
                            "status": "进行中",
                            "create_time": get_current_date(),
                            "update_time": get_current_date()
                        }
                        st.success(f"统筹计划「{coord_name}」已创建！")


                        # 页面刷新
                        def rerun():
                            try:
                                st.rerun()
                            except AttributeError:
                                st.experimental_rerun()


                        rerun()

            # ========== 统筹计划列表 ==========
            st.markdown("---")
            st.subheader("📋 统筹计划列表")

            # 筛选当前项目的统筹计划
            project_coords = [
                p for p in st.session_state.coordination_plans.values()
                if p.get("project_id") == selected_proj_id
            ]
            project_coords.sort(key=lambda x: x.get("create_time", ""), reverse=True)

            if project_coords:
                import pandas as pd
                from datetime import datetime

                # 准备表格数据
                coord_table = []
                for idx, plan in enumerate(project_coords, 1):
                    # 计算计划进度
                    try:
                        start = datetime.strptime(plan["start_date"], "%Y-%m-%d")
                        end = datetime.strptime(plan["end_date"], "%Y-%m-%d")
                        today = datetime.now()
                        total_days = (end - start).days
                        elapsed_days = (today - start).days if today > start else 0
                        progress = min(100, max(0, int((elapsed_days / total_days) * 100))) if total_days > 0 else 0
                    except:
                        progress = 0

                    coord_table.append({
                        "序号": idx,
                        "计划名称": plan["name"],
                        "统筹类型": plan["type"],
                        "关联项目数": len(plan["related_projects"]),
                        "时间范围": f"{plan['start_date']} 至 {plan['end_date']}",
                        "负责人": plan["responsible"],
                        "状态": plan["status"],
                        "进度": progress,
                        "创建时间": plan["create_time"],
                        "操作ID": plan["id"]  # 用于后台操作
                    })

                # 展示表格
                df_coords = pd.DataFrame(coord_table)
                edited_df = st.data_editor(
                    df_coords.drop(columns=["操作ID"]),
                    use_container_width=True,
                    column_config={
                        "序号": st.column_config.NumberColumn(width="small"),
                        "计划名称": st.column_config.TextColumn(width="medium"),
                        "统筹类型": st.column_config.TextColumn(width="small"),
                        "关联项目数": st.column_config.NumberColumn(width="small"),
                        "时间范围": st.column_config.TextColumn(width="medium"),
                        "负责人": st.column_config.TextColumn(width="small"),
                        "状态": st.column_config.SelectboxColumn(
                            "状态",
                            width="small",
                            options=["未开始", "进行中", "已完成", "已暂停"],
                            required=True
                        ),
                        "进度": st.column_config.ProgressColumn(
                            "进度",
                            width="small",
                            min_value=0,
                            max_value=100,
                            format="%d%%"
                        ),
                        "创建时间": st.column_config.TextColumn(width="medium")
                    },
                    key="coord_editor"
                )

                # 保存状态更新
                if st.button("保存状态更新", type="secondary"):
                    # 建立名称→ID映射
                    name_to_id = {p["name"]: p["id"] for p in project_coords}


                    def get_current_date():
                        from datetime import datetime
                        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


                    for _, row in edited_df.iterrows():
                        coord_id = name_to_id.get(row["计划名称"])
                        if not coord_id:
                            continue

                        # 更新状态和进度
                        st.session_state.coordination_plans[coord_id].update({
                            "status": row["状态"],
                            "update_time": get_current_date()
                        })

                    st.success("统筹计划状态已更新！")


                    def rerun():
                        try:
                            st.rerun()
                        except AttributeError:
                            st.experimental_rerun()


                    rerun()

                # ========== 查看详情 ==========
                st.markdown("---")
                selected_coord_name = st.selectbox(
                    "选择计划查看详情",
                    [p["name"] for p in project_coords],
                    key="coord_detail_select"
                )
                selected_coord = next(p for p in project_coords if p["name"] == selected_coord_name)

                with st.expander("统筹计划详情", expanded=True):
                    col_detail1, col_detail2 = st.columns(2)
                    with col_detail1:
                        st.write(f"**计划ID**：{selected_coord['id']}")
                        st.write(f"**统筹类型**：{selected_coord['type']}")
                        st.write(f"**时间范围**：{selected_coord['start_date']} 至 {selected_coord['end_date']}")
                        st.write(f"**负责人**：{selected_coord['responsible']}")
                        st.write(f"**当前状态**：{selected_coord['status']}")
                    with col_detail2:
                        st.write(f"**创建时间**：{selected_coord['create_time']}")
                        st.write(f"**最后更新**：{selected_coord['update_time']}")
                        st.write(f"**关联项目**：{', '.join(selected_coord['related_projects'])}")

                    st.markdown("---")
                    st.write("**统筹目标**")
                    st.write(selected_coord['objective'])

                    st.markdown("---")
                    st.write("**统筹策略**")
                    st.write(selected_coord['strategy'])

                    # ========== 统筹日志记录 ==========
                    st.markdown("---")
                    st.subheader("统筹执行日志")

                    # 获取当前计划的日志
                    coord_logs = [
                        log for log in st.session_state.coord_logs.values()
                        if log.get("coord_id") == selected_coord["id"]
                    ]
                    coord_logs.sort(key=lambda x: x.get("log_time", ""), reverse=True)

                    # 添加日志
                    with st.form(key=f"coord_log_form_{selected_coord['id']}"):
                        log_content = st.text_area("记录执行情况",
                                                   placeholder="请输入本次统筹的执行进展、遇到的问题及解决方案...",
                                                   key="coord_log_content")
                        if st.form_submit_button("添加日志"):
                            if log_content.strip():
                                def generate_unique_id(prefix="COORD_LOG"):
                                    import uuid
                                    return f"{prefix}_{uuid.uuid4().hex[:8]}"


                                def get_current_date():
                                    from datetime import datetime
                                    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


                                st.session_state.username = st.session_state.get("username", "未知用户")

                                log_id = generate_unique_id("COORD_LOG")
                                st.session_state.coord_logs[log_id] = {
                                    "id": log_id,
                                    "coord_id": selected_coord["id"],
                                    "coord_name": selected_coord["name"],
                                    "content": log_content.strip(),
                                    "author": st.session_state.username,
                                    "log_time": get_current_date()
                                }
                                st.success("日志已添加！")


                                def rerun():
                                    try:
                                        st.rerun()
                                    except AttributeError:
                                        st.experimental_rerun()


                                rerun()

                    # 展示日志
                    if coord_logs:
                        for log in coord_logs:
                            with st.expander(
                                    f"[{log.get('log_time', '未知时间')}] {log.get('author', '未知用户')} 记录",
                                    expanded=False):
                                st.write(log.get("content", "无内容"))
                    else:
                        st.info("暂无执行日志，请添加统筹进展记录")
            else:
                st.info("当前项目暂无统筹计划，请点击「新增统筹计划」创建")
    # 3. 进度检测（保持占位）
    with proj_main_tab[2]:
        st.subheader("进度检测")
        st.markdown("---")

        # 初始化进度检测相关数据
        if "progress_records" not in st.session_state:
            st.session_state.progress_records = {}  # 进度填报记录
        if "detection_cycles" not in st.session_state:
            st.session_state.detection_cycles = {}  # 兼容检测周期数据
        if "selected_proj_id" not in st.session_state:
            st.session_state.selected_proj_id = ""
        if "selected_proj_name" not in st.session_state:
            st.session_state.selected_proj_name = ""


        # 工具函数（内置兼容）
        def generate_unique_id(prefix="PROGRESS"):
            import uuid
            return f"{prefix}_{uuid.uuid4().hex[:8]}"


        def get_current_date():
            from datetime import datetime
            return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


        def rerun():
            try:
                st.rerun()
            except AttributeError:
                st.experimental_rerun()


        def export_to_excel(df, filename):
            import pandas as pd
            import io
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='进度数据')
            buffer.seek(0)
            st.download_button(
                label="下载Excel文件",
                data=buffer,
                file_name=f"{filename}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )


        # 1. 项目选择
        col_proj, col_refresh = st.columns([3, 1])
        with col_proj:
            project_list = st.session_state.get("projects", {})
            if project_list:
                project_options = {p["name"]: p["id"] for p in project_list.values()}
                selected_proj_name = st.selectbox(
                    "选择项目",
                    list(project_options.keys()),
                    key="progress_proj_select"
                )
                selected_proj_id = project_options[selected_proj_name]
                st.session_state.selected_proj_id = selected_proj_id
                st.session_state.selected_proj_name = selected_proj_name
            else:
                st.warning("暂无项目数据，请先在项目管理中创建项目")
                st.stop()

        with col_refresh:
            if st.button("刷新数据", type="secondary"):
                rerun()

        st.markdown("---")

        # 2. 阶段选择（执行/数据分析）
        progress_tab1, progress_tab2 = st.tabs(["📝 执行阶段 - 进度填报", "📊 数据分析阶段 - 进度分析"])

        # ====================== 第一阶段：执行阶段 - 进度填报 ======================
        with progress_tab1:
            st.subheader("进度填报")

            # 获取当前项目的检测周期配置
            project_cycles = [
                cycle for cycle in st.session_state.detection_cycles.values()
                if cycle["project_id"] == selected_proj_id and cycle["status"] == "已生效"
            ]

            if not project_cycles:
                st.warning("当前项目暂无生效的检测周期配置，请先在「基础数据-检测周期定义」中创建")
            else:
                # 选择周期配置
                cycle_options = {cycle["name"]: cycle["id"] for cycle in project_cycles}
                selected_cycle_name = st.selectbox(
                    "选择检测周期配置",
                    list(cycle_options.keys()),
                    key="progress_cycle_select"
                )
                selected_cycle_id = cycle_options[selected_cycle_name]
                selected_cycle = next(cycle for cycle in project_cycles if cycle["id"] == selected_cycle_id)

                # 筛选可填报的子周期（未锁定、未结束）
                fillable_sub_cycles = [
                    sub for sub in selected_cycle["cycles_detail"]
                    if sub["status"] in ["未开始", "进行中"]
                ]

                if not fillable_sub_cycles:
                    st.info("当前无可用填报的子周期（所有子周期已锁定/结束）")
                else:
                    # 选择子周期
                    sub_cycle_options = {sub["sub_cycle_name"]: sub["sub_cycle_id"] for sub in fillable_sub_cycles}
                    selected_sub_cycle_name = st.selectbox(
                        "选择填报子周期",
                        list(sub_cycle_options.keys()),
                        key="progress_sub_cycle_select"
                    )
                    selected_sub_cycle_id = sub_cycle_options[selected_sub_cycle_name]
                    selected_sub_cycle = next(
                        sub for sub in fillable_sub_cycles if sub["sub_cycle_id"] == selected_sub_cycle_id)

                    st.markdown(
                        f"### 填报周期：{selected_sub_cycle_name}（{selected_sub_cycle['sub_cycle_start']} ~ {selected_sub_cycle['sub_cycle_end']}）")
                    st.markdown(f"**填报责任人**：{selected_sub_cycle['owner']}")
                    st.markdown("---")

                    # 获取当前项目的一级子计划（从plans中提取）
                    project_plans = [
                        p for p in st.session_state.get("plans", {}).values()
                        if p.get("project_id") == selected_proj_id
                    ]

                    # 进度填报表单
                    with st.form(key="progress_fill_form"):
                        st.subheader("1. 总计划进度填报")
                        col1, col2 = st.columns(2)
                        with col1:
                            total_plan_pv = st.number_input(
                                "本周期计划完成占比（%）",
                                min_value=0, max_value=100, step=1,
                                key="total_plan_pv",
                                help="本周期内总计划预计完成的工作量占比"
                            )
                        with col2:
                            total_plan_ev = st.number_input(
                                "本周期实际完成占比（%）",
                                min_value=0, max_value=100, step=1,
                                key="total_plan_ev",
                                help="本周期内总计划实际完成的工作量占比"
                            )

                        st.markdown("---")
                        st.subheader("2. 一级子计划进度填报")

                        # 子计划进度填报表格
                        plan_fill_data = []
                        if project_plans:
                            for idx, plan in enumerate(project_plans, 1):
                                plan_fill_data.append({
                                    "序号": idx,
                                    "子计划名称": plan["name"],
                                    "计划完成占比（%）": 0,
                                    "实际完成占比（%）": 0,
                                    "进度偏差说明": "",
                                    "plan_id": plan["id"]
                                })
                        else:
                            plan_fill_data.append({
                                "序号": 1,
                                "子计划名称": "默认子计划",
                                "计划完成占比（%）": 0,
                                "实际完成占比（%）": 0,
                                "进度偏差说明": "",
                                "plan_id": "default_plan"
                            })

                        import pandas as pd

                        df_plan_fill = pd.DataFrame(plan_fill_data)
                        edited_df = st.data_editor(
                            df_plan_fill.drop(columns=["plan_id"]),
                            use_container_width=True,
                            column_config={
                                "序号": st.column_config.NumberColumn(width="small", disabled=True),
                                "子计划名称": st.column_config.TextColumn(width="medium", disabled=True),
                                "计划完成占比（%）": st.column_config.NumberColumn(width="small", min_value=0,
                                                                                 max_value=100),
                                "实际完成占比（%）": st.column_config.NumberColumn(width="small", min_value=0,
                                                                                 max_value=100),
                                "进度偏差说明": st.column_config.TextColumn(width="large")
                            },
                            key="plan_fill_editor"
                        )

                        st.markdown("---")
                        st.subheader("3. 整体说明")
                        overall_note = st.text_area(
                            "本周期进度整体说明/偏差原因",
                            placeholder="请填写本周期进度偏差的原因、遇到的问题、后续措施等...",
                            key="overall_note",
                            height=100
                        )

                        # 提交按钮
                        col_submit, col_save = st.columns(2)
                        with col_submit:
                            submit_btn = st.form_submit_button("提交进度数据", type="primary")
                        with col_save:
                            save_btn = st.form_submit_button("暂存进度数据", type="secondary")

                        # 提交逻辑
                        if submit_btn or save_btn:
                            # 组装填报数据
                            progress_record_id = generate_unique_id("PROGRESS")
                            plan_detail_list = []

                            for _, row in edited_df.iterrows():
                                plan_id = df_plan_fill[df_plan_fill["子计划名称"] == row["子计划名称"]]["plan_id"].iloc[
                                    0]
                                plan_detail_list.append({
                                    "plan_id": plan_id,
                                    "plan_name": row["子计划名称"],
                                    "pv": row["计划完成占比（%）"],
                                    "ev": row["实际完成占比（%）"],
                                    "spi": row["实际完成占比（%）"] / row["计划完成占比（%）"] if row[
                                                                                                  "计划完成占比（%）"] > 0 else 0,
                                    "note": row["进度偏差说明"]
                                })

                            # 计算总SPI
                            total_spi = total_plan_ev / total_plan_pv if total_plan_pv > 0 else 0

                            # 保存数据
                            st.session_state.progress_records[progress_record_id] = {
                                "id": progress_record_id,
                                "project_id": selected_proj_id,
                                "project_name": selected_proj_name,
                                "cycle_config_id": selected_cycle_id,
                                "cycle_config_name": selected_cycle_name,
                                "sub_cycle_id": selected_sub_cycle_id,
                                "sub_cycle_name": selected_sub_cycle_name,
                                "sub_cycle_start": selected_sub_cycle["sub_cycle_start"],
                                "sub_cycle_end": selected_sub_cycle["sub_cycle_end"],
                                "total_pv": total_plan_pv,
                                "total_ev": total_plan_ev,
                                "total_spi": round(total_spi, 2),
                                "plan_details": plan_detail_list,
                                "overall_note": overall_note,
                                "submitter": st.session_state.get("username", "未知用户"),
                                "submit_time": get_current_date(),
                                "status": "已提交" if submit_btn else "暂存"
                            }

                            # 更新子周期状态（提交后改为进行中）
                            if submit_btn:
                                for sub in selected_cycle["cycles_detail"]:
                                    if sub["sub_cycle_id"] == selected_sub_cycle_id:
                                        sub["status"] = "进行中"
                                        break
                                st.success("进度数据已提交！")
                            else:
                                st.success("进度数据已暂存！")
                            rerun()

                # 已填报记录查看
                st.markdown("---")
                st.subheader("已填报/暂存记录")

                # 筛选当前项目的填报记录
                progress_records = [
                    rec for rec in st.session_state.progress_records.values()
                    if rec["project_id"] == selected_proj_id
                ]

                if progress_records:
                    record_table = []
                    for idx, rec in enumerate(progress_records, 1):
                        # 预处理SPI值：确保是字符串/数字，避免空值/非数字导致校验失败
                        total_spi = rec.get("total_spi", "")
                        if total_spi == "" or pd.isna(total_spi):
                            total_spi = "未计算"
                        else:
                            total_spi = str(total_spi)  # 统一转为字符串，避免类型冲突

                        record_table.append({
                            "序号": idx,  # 底层是整数
                            "填报周期": rec.get("sub_cycle_name", ""),
                            "总计划SPI": total_spi,
                            "填报状态": rec.get("status", ""),
                            "填报人": rec.get("submitter", ""),
                            "填报时间": rec.get("submit_time", ""),
                            "操作ID": rec.get("id", "")
                        })

                    df_records = pd.DataFrame(record_table)
                    # 安全删除列：只删存在的列，避免KeyError
                    drop_cols = [col for col in ["操作ID"] if col in df_records.columns]
                    df_records_clean = df_records.drop(columns=drop_cols)

                    # 填充空值：避免类型校验报错
                    df_records_clean = df_records_clean.fillna("").replace("nan", "")

                    # 核心修复：序号列用NumberColumn（匹配底层INTEGER类型）
                    st.data_editor(
                        df_records_clean,
                        use_container_width=True,
                        disabled=True,  # 禁用编辑，降低校验严格度
                        hide_index=True,  # 隐藏索引，避免额外校验
                        column_config={
                            # 修复：序号列用NumberColumn（匹配整数类型）
                            "序号": st.column_config.NumberColumn(
                                width="small",
                                disabled=True,  # 禁用编辑，避免类型校验
                                required=False  # 关闭必填校验
                            ),
                            "填报周期": st.column_config.TextColumn(width="medium", disabled=True),
                            "总计划SPI": st.column_config.TextColumn(width="small", disabled=True),
                            "填报状态": st.column_config.TextColumn(width="small", disabled=True),
                            "填报人": st.column_config.TextColumn(width="small", disabled=True),
                            "填报时间": st.column_config.TextColumn(width="medium", disabled=True)
                        }
                    )
                else:
                    st.info("暂无进度填报记录")
        # ====================== 第二阶段：数据分析阶段 - 进度分析 ======================
        with progress_tab2:
            st.subheader("进度数据分析")

            # 获取当前项目的进度记录
            progress_records = [
                rec for rec in st.session_state.progress_records.values()
                if rec["project_id"] == selected_proj_id and rec["status"] == "已提交"
            ]

            if not progress_records:
                st.warning("当前项目暂无已提交的进度数据，请先在「执行阶段」填报数据")
            else:
                # 按子周期排序
                progress_records.sort(key=lambda x: x["sub_cycle_start"])

                # 1. 总览分析
                st.markdown("### 1. 项目整体进度总览")

                # 计算累计数据
                total_pv_sum = sum([rec["total_pv"] for rec in progress_records])
                total_ev_sum = sum([rec["total_ev"] for rec in progress_records])
                avg_spi = total_ev_sum / total_pv_sum if total_pv_sum > 0 else 0
                avg_spi = round(avg_spi, 2)

                # 总览卡片
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric(
                        label="累计计划完成占比（PV）",
                        value=f"{total_pv_sum}%",
                        delta=f"共{len(progress_records)}个周期"
                    )
                with col2:
                    st.metric(
                        label="累计实际完成占比（EV）",
                        value=f"{total_ev_sum}%",
                        delta=f"{total_ev_sum - total_pv_sum}%"
                    )
                with col3:
                    # SPI状态颜色
                    if avg_spi >= 1:
                        spi_color = "green"
                        spi_status = "进度超前"
                    elif 0.9 <= avg_spi < 1:
                        spi_color = "orange"
                        spi_status = "进度轻微滞后"
                    else:
                        spi_color = "red"
                        spi_status = "进度严重滞后"

                    st.markdown(f"""
                        <div style='background-color:#f0f2f6;padding:16px;border-radius:8px;text-align:center'>
                            <p style='font-size:14px;margin:0;color:#666'>整体进度绩效指数（SPI）</p>
                            <p style='font-size:28px;margin:4px 0;color:{spi_color};font-weight:bold'>{avg_spi}</p>
                            <p style='font-size:12px;margin:0;color:#666'>{spi_status}</p>
                        </div>
                    """, unsafe_allow_html=True)

                st.markdown("---")

                # 赢得值曲线（累计）
                st.subheader("2. 累计赢得值曲线")

                # 准备曲线数据
                x_data = [rec["sub_cycle_name"] for rec in progress_records]
                pv_data = [sum([r["total_pv"] for r in progress_records[:i + 1]]) for i in range(len(progress_records))]
                ev_data = [sum([r["total_ev"] for r in progress_records[:i + 1]]) for i in range(len(progress_records))]

                import plotly.express as px
                import plotly.graph_objects as go

                fig = go.Figure()
                # PV曲线
                fig.add_trace(go.Scatter(
                    x=x_data, y=pv_data,
                    name="累计计划值（PV）",
                    line=dict(color="#1f77b4", width=2),
                    hovertemplate="周期：%{x}<br>累计PV：%{y}%<extra></extra>"
                ))
                # EV曲线
                fig.add_trace(go.Scatter(
                    x=x_data, y=ev_data,
                    name="累计赢得值（EV）",
                    line=dict(color="#2ca02c", width=2, dash="dash"),
                    hovertemplate="周期：%{x}<br>累计EV：%{y}%<br>SPI：%{customdata}<extra></extra>",
                    customdata=[round(ev_data[i] / pv_data[i], 2) if pv_data[i] > 0 else 0 for i in range(len(ev_data))]
                ))

                fig.update_layout(
                    title="项目累计PV/EV对比曲线",
                    xaxis_title="检测周期",
                    yaxis_title="累计完成占比（%）",
                    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)

                st.markdown("---")

                # 3. 周期数据分析
                st.subheader("3. 周期级进度分析")

                # 周期选择
                col_select, col_export = st.columns([3, 1])
                with col_select:
                    cycle_analysis_type = st.radio(
                        "分析类型",
                        ["单周期详情", "多周期趋势"],
                        key="cycle_analysis_type",
                        horizontal=True
                    )

                with col_export:
                    # 导出周期数据（表单外普通按钮）
                    if st.button("导出周期数据", type="secondary", key="export_cycle_data"):
                        export_data = []
                        for rec in progress_records:
                            export_data.append({
                                "项目名称": rec["project_name"],
                                "检测周期": rec["sub_cycle_name"],
                                "周期开始时间": rec["sub_cycle_start"],
                                "周期结束时间": rec["sub_cycle_end"],
                                "本周期PV（%）": rec["total_pv"],
                                "本周期EV（%）": rec["total_ev"],
                                "本周期SPI": rec["total_spi"],
                                "累计PV（%）": sum([r["total_pv"] for r in progress_records if
                                                  r["sub_cycle_start"] <= rec["sub_cycle_start"]]),
                                "累计EV（%）": sum([r["total_ev"] for r in progress_records if
                                                  r["sub_cycle_start"] <= rec["sub_cycle_start"]]),
                                "累计SPI": round(sum([r["total_ev"] for r in progress_records if
                                                      r["sub_cycle_start"] <= rec["sub_cycle_start"]]) /
                                                 sum([r["total_pv"] for r in progress_records if
                                                      r["sub_cycle_start"] <= rec["sub_cycle_start"]])
                                                 if sum([r["total_pv"] for r in progress_records if
                                                         r["sub_cycle_start"] <= rec["sub_cycle_start"]]) > 0 else 0,
                                                 2),
                                "偏差说明": rec["overall_note"],
                                "填报人": rec["submitter"],
                                "填报时间": rec["submit_time"]
                            })

                        df_export = pd.DataFrame(export_data)
                        export_to_excel(df_export,
                                        f"{selected_proj_name}_进度分析报告_{get_current_date().split(' ')[0]}")

                # 3.1 单周期详情
                if cycle_analysis_type == "单周期详情":
                    cycle_options = {rec["sub_cycle_name"]: rec["id"] for rec in progress_records}
                    selected_analysis_cycle = st.selectbox(
                        "选择分析周期",
                        list(cycle_options.keys()),
                        key="selected_analysis_cycle"
                    )
                    selected_record = next(
                        rec for rec in progress_records if rec["sub_cycle_name"] == selected_analysis_cycle)

                    # 单周期核心数据
                    st.markdown(f"#### 周期详情：{selected_record['sub_cycle_name']}")
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("本周期PV", f"{selected_record['total_pv']}%")
                    with col2:
                        st.metric("本周期EV", f"{selected_record['total_ev']}%")
                    with col3:
                        st.metric("本周期SPI", selected_record['total_spi'])
                    with col4:
                        # 累计SPI
                        cumulative_pv = sum([r["total_pv"] for r in progress_records if
                                             r["sub_cycle_start"] <= selected_record["sub_cycle_start"]])
                        cumulative_ev = sum([r["total_ev"] for r in progress_records if
                                             r["sub_cycle_start"] <= selected_record["sub_cycle_start"]])
                        cumulative_spi = round(cumulative_ev / cumulative_pv if cumulative_pv > 0 else 0, 2)
                        st.metric("累计SPI", cumulative_spi)

                    # 子计划详情
                    st.markdown("##### 子计划进度明细")
                    plan_detail = selected_record["plan_details"]
                    plan_table = []
                    for idx, plan in enumerate(plan_detail, 1):
                        plan_table.append({
                            "序号": idx,
                            "子计划名称": plan["plan_name"],
                            "计划完成占比（%）": plan["pv"],
                            "实际完成占比（%）": plan["ev"],
                            "SPI": round(plan["spi"], 2),
                            "偏差说明": plan["note"]
                        })

                    df_plan_detail = pd.DataFrame(plan_table)
                    st.data_editor(
                        df_plan_detail,
                        use_container_width=True,
                        disabled=True,
                        column_config={
                            "序号": st.column_config.NumberColumn(width="small"),
                            "子计划名称": st.column_config.TextColumn(width="medium"),
                            "计划完成占比（%）": st.column_config.NumberColumn(width="small"),
                            "实际完成占比（%）": st.column_config.NumberColumn(width="small"),
                            "SPI": st.column_config.NumberColumn(width="small"),
                            "偏差说明": st.column_config.TextColumn(width="large")
                        }
                    )

                    # 整体说明
                    st.markdown("##### 周期整体说明")
                    st.text_area(
                        "",
                        value=selected_record["overall_note"],
                        height=100,
                        disabled=True
                    )

                # 3.2 多周期趋势
                else:
                    st.markdown("#### 多周期SPI趋势")

                    # SPI趋势图
                    x_data = [rec["sub_cycle_name"] for rec in progress_records]
                    spi_data = [rec["total_spi"] for rec in progress_records]
                    cumulative_spi_data = [
                        round(sum([r["total_ev"] for r in progress_records[:i + 1]]) / sum(
                            [r["total_pv"] for r in progress_records[:i + 1]]) if sum(
                            [r["total_pv"] for r in progress_records[:i + 1]]) > 0 else 0, 2)
                        for i in range(len(progress_records))
                    ]

                    fig_trend = go.Figure()
                    # 单周期SPI
                    fig_trend.add_trace(go.Bar(
                        x=x_data, y=spi_data,
                        name="单周期SPI",
                        marker_color="#1f77b4",
                        hovertemplate="周期：%{x}<br>单周期SPI：%{y}<extra></extra>"
                    ))
                    # 累计SPI
                    fig_trend.add_trace(go.Scatter(
                        x=x_data, y=cumulative_spi_data,
                        name="累计SPI",
                        line=dict(color="#ff7f0e", width=2),
                        hovertemplate="周期：%{x}<br>累计SPI：%{y}<extra></extra>"
                    ))
                    # 基准线（SPI=1）
                    fig_trend.add_hline(
                        y=1, line_dash="dash", line_color="green",
                        annotation_text="计划基准线（SPI=1）",
                        annotation_position="top right"
                    )

                    fig_trend.update_layout(
                        title="周期SPI趋势对比",
                        xaxis_title="检测周期",
                        yaxis_title="SPI值",
                        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                        height=400
                    )
                    st.plotly_chart(fig_trend, use_container_width=True)

                    # 周期对比表
                    st.markdown("#### 周期对比明细表")
                    cycle_table = []
                    for idx, rec in enumerate(progress_records, 1):
                        cumulative_pv = sum([r["total_pv"] for r in progress_records[:idx]])
                        cumulative_ev = sum([r["total_ev"] for r in progress_records[:idx]])
                        cumulative_spi = round(cumulative_ev / cumulative_pv if cumulative_pv > 0 else 0, 2)

                        cycle_table.append({
                            "序号": idx,
                            "检测周期": rec["sub_cycle_name"],
                            "本周期PV（%）": rec["total_pv"],
                            "本周期EV（%）": rec["total_ev"],
                            "本周期SPI": rec["total_spi"],
                            "累计PV（%）": cumulative_pv,
                            "累计EV（%）": cumulative_ev,
                            "累计SPI": cumulative_spi,
                            "偏差说明": rec["overall_note"][:50] + "..." if len(rec["overall_note"]) > 50 else rec[
                                "overall_note"]
                        })

                    df_cycle = pd.DataFrame(cycle_table)
                    st.data_editor(
                        df_cycle,
                        use_container_width=True,
                        disabled=True,
                        column_config={
                            "序号": st.column_config.NumberColumn(width="small"),
                            "检测周期": st.column_config.TextColumn(width="medium"),
                            "本周期PV（%）": st.column_config.NumberColumn(width="small"),
                            "本周期EV（%）": st.column_config.NumberColumn(width="small"),
                            "本周期SPI": st.column_config.NumberColumn(width="small"),
                            "累计PV（%）": st.column_config.NumberColumn(width="small"),
                            "累计EV（%）": st.column_config.NumberColumn(width="small"),
                            "累计SPI": st.column_config.NumberColumn(width="small"),
                            "偏差说明": st.column_config.TextColumn(width="large")
                        }
                    )


        # ====================== 全局工具函数（提前定义，避免嵌套） ======================
        def generate_unique_id(prefix="MONITOR"):
            import uuid
            return f"{prefix}_{uuid.uuid4().hex[:8]}"


        def get_current_date():
            from datetime import datetime
            return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


        def rerun():
            try:
                st.rerun()
            except AttributeError:
                st.experimental_rerun()


        def export_to_excel(df, filename):
            import pandas as pd
            import io
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='监控数据')
            buffer.seek(0)
            st.download_button(
                label="下载Excel文件",
                data=buffer,
                file_name=f"{filename}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )


        # ====================== 全局工具函数（提前定义） ======================
        def get_current_date():
            from datetime import datetime
            return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


        def rerun():
            try:
                st.rerun()
            except AttributeError:
                st.experimental_rerun()


        # ========== 核心：邮件发送函数（修复From字段问题） ==========
        def send_progress_email(to_emails, project_name, notice_title, notice_content, spi, delay_days):
            import smtplib
            import ssl
            from email.mime.text import MIMEText
            from email.header import Header

            # 163邮箱核心配置
            smtp_server = "smtp.163.com"
            smtp_port = 465
            sender_email = "18526367457@163.com"
            sender_auth = "AAVPx38aKaASPUVG"

            # 过滤无效邮箱
            valid_emails = [email.strip() for email in to_emails if "@" in email.strip()]
            if not valid_emails:
                st.warning("未找到有效邮箱，邮件发送失败！")
                return False

            # 邮件内容
            email_content = f"""
            <html>
                <body style='font-family:Arial,sans-serif;line-height:1.6'>
                    <h2 style='color:#2563eb'>【项目进度预警】{project_name}</h2>
                    <div style='background-color:#f8fafc;padding:16px;border-radius:8px;margin:16px 0'>
                        <p style='margin:8px 0'><strong>当前SPI值：</strong>{spi}</p>
                        <p style='margin:8px 0'><strong>进度滞后天数：</strong>{delay_days}天</p>
                    </div>
                    <p style='margin:16px 0'><strong>预警原因：</strong>{notice_content}</p>
                    <hr style='margin:24px 0;border:none;border-top:1px solid #e2e8f0'>
                    <p style='color:#94a3b8;font-size:14px;margin:0'>此邮件由PMP系统自动发送，请勿回复</p>
                </body>
            </html>
            """

            # 核心修复：简化From字段，只保留发件人邮箱
            msg = MIMEText(email_content, "html", "utf-8")
            msg["From"] = sender_email  # 去掉别名，直接用邮箱，避免格式错误
            msg["To"] = ",".join(valid_emails)  # 去掉Header包装，简化格式
            msg["Subject"] = Header(f"【进度预警】{project_name}", "utf-8")  # Subject保留Header，保证中文显示

            try:
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context, timeout=30) as server:
                    server.login(sender_email, sender_auth)
                    for email in valid_emails:
                        server.sendmail(sender_email, [email], msg.as_string())
                st.success(f"✅ 预警邮件已发送至：{', '.join(valid_emails)}")
                return True
            except smtplib.SMTPAuthenticationError:
                st.error("❌ 邮件发送失败：授权码错误（请检查163邮箱授权码）")
                return False
            except smtplib.SMTPConnectError:
                st.error("❌ 邮件发送失败：网络/端口被封禁（切换手机热点试试）")
                return False
            except smtplib.SMTPServerDisconnected:
                st.error("❌ 邮件发送失败：连接被服务器关闭（授权码/端口错误）")
                return False
            except Exception as e:
                st.error(f"❌ 邮件发送失败：{str(e)}")
                import traceback
                st.text(f"详细错误：{traceback.format_exc()}")
                return False


        # ====================== 进度监控标签页（无改动） ======================
        with proj_main_tab[3]:
            st.subheader("进度监控 & 邮件预警")
            st.markdown("---")

            # 初始化必要数据
            if "warn_rules" not in st.session_state:
                st.session_state.warn_rules = {}
            if "auto_warn_sent" not in st.session_state:
                st.session_state.auto_warn_sent = {}

            # 1. 项目选择
            col_proj, col_refresh = st.columns([3, 1])
            with col_proj:
                project_list = st.session_state.get("projects", {})
                if not project_list:
                    st.warning("暂无项目数据，请先创建项目")
                    st.stop()

                project_options = {p["name"]: p["id"] for p in project_list.values()}
                selected_proj_name = st.selectbox(
                    "选择监控项目",
                    list(project_options.keys()),
                    key="monitor_proj_email_warn"
                )
                selected_proj_id = project_options[selected_proj_name]

            with col_refresh:
                if st.button("刷新数据", type="secondary", key="btn_refresh_email_warn"):
                    rerun()

            st.markdown("---")

            # 2. 读取进度数据
            progress_records = [
                rec for rec in st.session_state.get("progress_records", {}).values()
                if rec["project_id"] == selected_proj_id and rec["status"] == "已提交"
            ]
            if not progress_records:
                st.warning("当前项目暂无进度数据，请先填报")
                st.stop()

            # 计算核心指标
            total_pv = sum([rec["total_pv"] for rec in progress_records])
            total_ev = sum([rec["total_ev"] for rec in progress_records])
            current_spi = round(total_ev / total_pv if total_pv > 0 else 0, 2)

            # 计算滞后天数
            delay_days = 0
            project_info = next((p for p in st.session_state.projects.values() if p["id"] == selected_proj_id), None)
            if project_info and "start_date" in project_info and "end_date" in project_info:
                from datetime import datetime

                try:
                    start = datetime.strptime(project_info["start_date"], "%Y-%m-%d")
                    end = datetime.strptime(project_info["end_date"], "%Y-%m-%d")
                    total_days = (end - start).days
                    planned_days = (total_pv / 100) * total_days
                    actual_days = (total_ev / 100) * total_days
                    delay_days = round(planned_days - actual_days, 1)
                except:
                    delay_days = 0

            # 3. 预警规则 + 邮件接收人配置
            st.markdown("### 1. 预警规则 & 邮件配置")
            col1, col2 = st.columns(2)
            with col1:
                proj_warn = st.session_state.warn_rules.get(selected_proj_id, {})
                warn_spi = st.number_input(
                    "SPI预警阈值（低于此值触发邮件）",
                    min_value=0.0, max_value=1.0, step=0.05,
                    value=proj_warn.get("spi_threshold", 0.9),
                    key="input_warn_spi_email"
                )
                warn_days = st.number_input(
                    "滞后天数预警阈值",
                    min_value=1, max_value=30, step=1,
                    value=proj_warn.get("delay_days", 3),
                    key="input_warn_days_email"
                )

                if st.button("保存预警规则", type="secondary", key="btn_save_warn_rule_email"):
                    st.session_state.warn_rules[selected_proj_id] = {
                        "spi_threshold": warn_spi,
                        "delay_days": warn_days,
                        "update_time": get_current_date()
                    }
                    st.success("预警规则已保存！")

            with col2:
                st.markdown("#### 邮件接收人")
                employee_list = st.session_state.get("employees", {})
                all_emails = []

                for emp in employee_list.values():
                    contact = emp.get("contact", "").strip()
                    if contact and "@" in contact:
                        all_emails.append(contact)

                if all_emails:
                    st.write(f"✅ 已同步 {len(all_emails)} 个有效邮箱：")
                    st.write(", ".join(all_emails))
                    extra_email = st.text_input(
                        "添加额外邮箱（逗号分隔）",
                        key="input_extra_email_warn"
                    )
                    if extra_email:
                        all_emails += [e.strip() for e in extra_email.split(",") if e.strip() and "@" in e]
                else:
                    st.warning("系统无有效邮箱，请手动输入")
                    manual_emails = st.text_input(
                        "手动输入接收人邮箱（逗号分隔）",
                        key="input_manual_email_warn"
                    )
                    if manual_emails:
                        all_emails = [e.strip() for e in manual_emails.split(",") if e.strip() and "@" in e]

            st.markdown("---")

            # 4. 实时预警 + 自动发送邮件
            st.markdown("### 2. 🔔 实时进度预警")
            warn_trigger = False
            warn_reason = ""

            if current_spi < warn_spi:
                warn_trigger = True
                warn_reason += f"SPI={current_spi} 低于阈值{warn_spi}；"
            if delay_days >= warn_days:
                warn_trigger = True
                warn_reason += f"进度滞后{delay_days}天 超过阈值{warn_days}天；"

            if warn_trigger:
                st.error(f"""
                    ⚠️ 进度预警触发！
                    原因：{warn_reason}
                """)

                warn_key = f"{selected_proj_id}_{current_spi}_{delay_days}"
                if warn_key not in st.session_state.auto_warn_sent and all_emails:
                    st.markdown("#### 正在自动发送预警邮件...")
                    send_success = send_progress_email(
                        to_emails=all_emails,
                        project_name=selected_proj_name,
                        notice_title="进度滞后预警",
                        notice_content=warn_reason,
                        spi=current_spi,
                        delay_days=delay_days
                    )
                    if send_success:
                        st.session_state.auto_warn_sent[warn_key] = True
            else:
                st.success(f"""
                    ✅ 进度正常
                    当前SPI：{current_spi} | 滞后天数：{delay_days}天
                """)

            # 5. 手动发送邮件按钮
            st.markdown("---")
            st.markdown("### 3. 📤 手动发送预警邮件")
            if st.button("手动发送预警邮件", type="primary", key="btn_manual_send_email_warn"):
                if not all_emails:
                    st.warning("请先配置邮件接收人！")
                else:
                    send_progress_email(
                        to_emails=all_emails,
                        project_name=selected_proj_name,
                        notice_title="手动触发-进度预警",
                        notice_content=f"手动发送预警：SPI={current_spi}，滞后天数={delay_days}天",
                        spi=current_spi,
                        delay_days=delay_days
                    )

        # 侧边栏底部信息
        st.sidebar.markdown("---")
