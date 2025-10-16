import streamlit as st
from pathlib import Path
import sqlite3
import pandas as pd
from datetime import datetime, date, time
import io

st.set_page_config(page_title="个人信息管理系统（数据库版）", page_icon="📋", layout="wide")

st.markdown("""
    <style>
    .stCard {
        background-color: #f8f9fa;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        margin-bottom: 25px;
    }
    .mainTitle {
        color: #2c3e50;
        font-weight: 600;
        margin-bottom: 30px;
        border-left: 4px solid #3498db;
        padding-left: 15px;
    }
    .subTitle {
        color: #34495e;
        font-weight: 500;
        margin: 15px 0 10px 0;
        border-bottom: 1px solid #eee;
        padding-bottom: 5px;
    }
    .stButton > button {
        background-color: #3498db;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 8px 16px;
        transition: all 0.2s;
    }
    .stButton > button:hover {
        background-color: #2980b9;
        transform: translateY(-1px);
    }
    .deleteBtn > button {
        background-color: #e74c3c !important;
    }
    .deleteBtn > button:hover {
        background-color: #c0392b !important;
    }
    .updateBtn > button {
        background-color: #2ecc71 !important;
    }
    .updateBtn > button:hover {
        background-color: #27ae60 !important;
    }
    .history-item {
        padding: 8px 0;
        border-bottom: 1px dashed #eee;
    }
    .history-time {
        color: #7f8c8d;
        font-size: 0.85rem;
    }
    </style>
""", unsafe_allow_html=True)


def init_db():

    try:
        conn = sqlite3.connect("personal_info.db")
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_profile (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT,
                create_time TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
            )
        ''')


        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_achievements (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                award_name TEXT NOT NULL,
                award_type TEXT NOT NULL,
                award_date TEXT NOT NULL,
                award_organization TEXT,
                award_description TEXT,
                FOREIGN KEY (user_id) REFERENCES user_profile(id) ON DELETE CASCADE
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_schedule (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                event_title TEXT NOT NULL,
                event_date TEXT NOT NULL,
                event_location TEXT,
                event_description TEXT,
                FOREIGN KEY (user_id) REFERENCES user_profile(id) ON DELETE CASCADE
            )
        ''')

        conn.commit()
        return conn
    except sqlite3.Error as e:
        st.error(f"数据库初始化失败：{str(e)}")
        st.stop()


def save_operation(operation, details):

    HISTORY_PATH = Path("operation_history.csv")
    HISTORY_COLUMNS = ["time", "operation", "details"]

    try:
        if HISTORY_PATH.exists():
            history_df = pd.read_csv(HISTORY_PATH)
        else:
            history_df = pd.DataFrame(columns=HISTORY_COLUMNS)

        new_record = pd.DataFrame([{
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operation": operation,
            "details": details
        }])

        updated_df = pd.concat([new_record, history_df], ignore_index=True).head(10)
        updated_df.to_csv(HISTORY_PATH, index=False, encoding="utf-8-sig")
    except Exception as e:
        st.warning(f"操作历史保存失败：{str(e)}")


def export_to_csv(df, filename_prefix):

    try:
        buffer = io.StringIO()
        df_clean = df.fillna("")
        df_clean.to_csv(buffer, index=False, encoding="utf-8-sig")
        buffer.seek(0)
        binary_data = buffer.getvalue().encode("utf-8-sig")
        filename = f"{filename_prefix}_{datetime.now().strftime('%Y%m%d')}.csv"
        return binary_data, filename
    except Exception as e:
        st.error(f"数据导出失败：{str(e)}")
        return None, None


def custom_date_time(default=None):

    if default is None:
        default = datetime.now()

    col1, col2 = st.columns(2)
    with col1:
        selected_date = st.date_input("选择日期", default.date())
    with col2:
        selected_time = st.time_input("选择时间", default.time())

    combined_datetime = datetime.combine(selected_date, selected_time)
    return combined_datetime


st.markdown('<h1 class="mainTitle">📋 个人信息管理系统（多表数据库版）</h1>', unsafe_allow_html=True)

conn = init_db()
cursor = conn.cursor()

menu = st.sidebar.selectbox(
    "功能菜单",
    ["1. 个人基本信息管理", "2. 个人荣誉管理", "3. 个人日程管理", "4. 操作历史"]
)

if menu == "1. 个人基本信息管理":
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    st.markdown('<h3 class="subTitle">➕ 新增个人基本信息</h3>', unsafe_allow_html=True)

    with st.form("add_profile_form", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            name = st.text_input("姓名*", placeholder="请输入真实姓名")
        with col2:
            phone = st.text_input("手机号", placeholder="如：13800138000")
        with col3:
            email = st.text_input("邮箱", placeholder="如：example@xxx.com")

        submitted_add = st.form_submit_button("确认新增")
        if submitted_add:
            if not name.strip():
                st.error("❌ 姓名不能为空！")
            else:
                try:
                    cursor.execute('''
                        INSERT INTO user_profile (name, phone, email)
                        VALUES (?, ?, ?)
                    ''', (name.strip(), phone.strip(), email.strip()))
                    conn.commit()
                    save_operation("新增个人信息", f"姓名：{name.strip()}，手机号：{phone.strip()}")
                    st.success("✅ 个人信息新增成功！")
                except sqlite3.Error as e:
                    st.error(f"新增失败：{str(e)}")

    st.markdown('<h3 class="subTitle">🔍 查看/导出个人基本信息</h3>', unsafe_allow_html=True)

    try:
        cursor.execute("SELECT * FROM user_profile ORDER BY id DESC")
        data = cursor.fetchall()
        if not data:
            st.info("ℹ️ 暂无个人基本信息，请先新增记录")
        else:
            profile_df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
            st.dataframe(
                profile_df,
                use_container_width=True,
                column_config={
                    "id": st.column_config.NumberColumn("ID", width="small"),
                    "name": st.column_config.TextColumn("姓名", width="medium"),
                    "phone": st.column_config.TextColumn("手机号", width="medium"),
                    "email": st.column_config.TextColumn("邮箱", width="large"),
                    "create_time": st.column_config.DatetimeColumn("创建时间", format="YYYY-MM-DD HH:mm")
                },
                hide_index=True
            )

            binary_data, filename = export_to_csv(profile_df, "个人基本信息")
            if binary_data and filename:
                st.download_button(
                    label="💾 导出CSV文件",
                    data=binary_data,
                    file_name=filename,
                    mime="text/csv"
                )
    except sqlite3.Error as e:
        st.error(f"查询失败：{str(e)}")

    st.markdown('<h3 class="subTitle">✏️ 更新/删除个人基本信息</h3>', unsafe_allow_html=True)

    try:
        cursor.execute("SELECT * FROM user_profile ORDER BY id DESC")
        data = cursor.fetchall()
        if not data:
            st.info("ℹ️ 暂无个人基本信息，无法进行更新/删除操作")
        else:
            profile_df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
            profile_ids = profile_df["id"].tolist()
            selected_id = st.selectbox("选择要操作的个人信息ID", profile_ids)

            cursor.execute("SELECT * FROM user_profile WHERE id = ?", (selected_id,))
            current_data = cursor.fetchone()
            if not current_data:
                st.error("❌ 选中的记录不存在！")
            else:
                current_name, current_phone, current_email = current_data[1], current_data[2], current_data[3]

                st.markdown('<h4 style="margin-top:10px;">更新信息</h4>', unsafe_allow_html=True)
                with st.form("update_profile_form", clear_on_submit=False):
                    new_name = st.text_input("姓名*", value=current_name)
                    new_phone = st.text_input("手机号", value=current_phone)
                    new_email = st.text_input("邮箱", value=current_email)

                    submitted_update = st.form_submit_button("确认更新", key="update_btn")
                    if submitted_update:
                        if not new_name.strip():
                            st.error("❌ 姓名不能为空！")
                        else:
                            try:
                                cursor.execute('''
                                    UPDATE user_profile
                                    SET name = ?, phone = ?, email = ?
                                    WHERE id = ?
                                ''', (new_name.strip(), new_phone.strip(), new_email.strip(), selected_id))
                                conn.commit()
                                save_operation("更新个人信息", f"ID：{selected_id}，新姓名：{new_name.strip()}")
                                st.success(f"✅ ID {selected_id} 的个人信息更新成功！")
                                st.experimental_rerun()
                            except sqlite3.Error as e:
                                st.error(f"更新失败：{str(e)}")

                st.markdown('<h4 style="margin-top:10px;">删除信息</h4>', unsafe_allow_html=True)
                st.warning("⚠️ 注意：删除个人信息后，关联的荣誉和日程记录也会被自动删除！")
                delete_btn = st.button("确认删除", key="delete_profile_btn")
                if delete_btn:
                    try:
                        cursor.execute("DELETE FROM user_profile WHERE id = ?", (selected_id,))
                        conn.commit()
                        save_operation("删除个人信息", f"ID：{selected_id}，姓名：{current_name}")
                        st.success(f"✅ ID {selected_id} 的个人信息已删除！")
                        st.experimental_rerun()
                    except sqlite3.Error as e:
                        st.error(f"删除失败：{str(e)}")
    except sqlite3.Error as e:
        st.error(f"操作失败：{str(e)}")

    st.markdown('</div>', unsafe_allow_html=True)


elif menu == "2. 个人荣誉管理":
    st.markdown('<div class="stCard">', unsafe_allow_html=True)

    try:
        cursor.execute("SELECT id, name FROM user_profile ORDER BY id DESC")
        user_list = cursor.fetchall()
        if not user_list:
            st.error("❌ 请先在【个人基本信息管理】中添加用户！")
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            user_dict = {str(user[0]): user[1] for user in user_list}
            user_options = [f"ID:{uid} - {name}" for uid, name in user_list]

            st.markdown('<h3 class="subTitle">➕ 新增个人荣誉</h3>', unsafe_allow_html=True)
            with st.form("add_achievement_form", clear_on_submit=True):
                col1, col2 = st.columns(2)
                with col1:
                    selected_user_option = st.selectbox("关联用户*", user_options)
                    award_name = st.text_input("荣誉名称*", placeholder="如：三好学生")

                    award_type = st.selectbox(
                        "荣誉类别*",
                        ["荣誉", "教育经历", "竞赛", "证书", "账号", "其他"]
                    )
                with col2:
                    award_date = st.date_input("获得日期*")
                    award_organization = st.text_input("颁发机构", placeholder="如：XX学校")

                award_description = st.text_area("荣誉描述", placeholder="请输入荣誉的详细说明...", height=80)
                submitted_add = st.form_submit_button("确认新增")

                if submitted_add:
                    if not award_name.strip():
                        st.error("❌ 荣誉名称不能为空！")
                    else:
                        try:
                            selected_uid = selected_user_option.split(" - ")[0].replace("ID:", "")
                            selected_uname = user_dict[selected_uid]
                            cursor.execute('''
                                INSERT INTO user_achievements 
                                (user_id, award_name, award_type, award_date, award_organization, award_description)
                                VALUES (?, ?, ?, ?, ?, ?)
                            ''', (selected_uid, award_name.strip(), award_type,
                                  award_date.strftime("%Y-%m-%d"), award_organization.strip(),
                                  award_description.strip()))
                            conn.commit()
                            save_operation("新增荣誉", f"用户：{selected_uname}，荣誉：{award_name.strip()}，类别：{award_type}")
                            st.success("✅ 个人荣誉新增成功！")
                        except sqlite3.Error as e:
                            st.error(f"新增失败：{str(e)}")

            st.markdown('<h3 class="subTitle">🔍 查看/筛选个人荣誉</h3>', unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)
            with col1:
                filter_uid = st.selectbox("按用户筛选", ["全部"] + user_options)
            with col2:
                filter_type = st.selectbox(
                    "按类别筛选",
                    ["全部", "荣誉", "教育经历", "竞赛", "证书", "账号", "其他"]
                )
            with col3:
                filter_keyword = st.text_input("关键词搜索", placeholder="搜索荣誉名称/描述...")

            try:

                conditions = []
                params = []
                if filter_uid != "全部":
                    filter_uid_val = filter_uid.split(" - ")[0].replace("ID:", "")
                    conditions.append("user_id = ?")
                    params.append(filter_uid_val)
                if filter_type != "全部":
                    conditions.append("award_type = ?")
                    params.append(filter_type)

                if conditions:
                    query_sql = f"SELECT * FROM user_achievements WHERE {' AND '.join(conditions)} ORDER BY id DESC"
                else:
                    query_sql = "SELECT * FROM user_achievements ORDER BY id DESC"

                cursor.execute(query_sql, params)
                achievement_df = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                if filter_keyword.strip() and not achievement_df.empty:
                    achievement_df = achievement_df[
                        achievement_df["award_name"].str.contains(filter_keyword.strip(), case=False, na=False) |
                        achievement_df["award_description"].str.contains(filter_keyword.strip(), case=False, na=False)
                    ]

                if not achievement_df.empty:

                    achievement_df["user_name"] = achievement_df["user_id"].astype(str).map(user_dict)
                    achievement_df = achievement_df[["id", "user_name", "award_type", "award_name",
                                                     "award_date", "award_organization", "award_description"]]

                    st.dataframe(
                        achievement_df,
                        use_container_width=True,
                        column_config={
                            "id": st.column_config.NumberColumn("荣誉ID", width="small"),
                            "user_name": st.column_config.TextColumn("关联用户", width="medium"),
                            "award_type": st.column_config.TextColumn("荣誉类别", width="medium"),
                            "award_name": st.column_config.TextColumn("荣誉名称", width="medium"),
                            "award_date": st.column_config.DateColumn("获得日期", width="medium"),
                            "award_organization": st.column_config.TextColumn("颁发机构", width="medium"),
                            "award_description": st.column_config.TextColumn("荣誉描述", width="large")
                        },
                        hide_index=True
                    )

                    binary_data, filename = export_to_csv(achievement_df, "个人荣誉记录")
                    if binary_data and filename:
                        st.download_button(
                            label="💾 导出CSV文件",
                            data=binary_data,
                            file_name=filename,
                            mime="text/csv"
                        )
                else:
                    st.info("ℹ️ 暂无符合条件的荣誉记录")
            except sqlite3.Error as e:
                st.error(f"查询失败：{str(e)}")

            st.markdown('<h3 class="subTitle">✏️ 更新/删除个人荣誉</h3>', unsafe_allow_html=True)
            if not achievement_df.empty:
                achievement_ids = achievement_df["id"].tolist()
                selected_ach_id = st.selectbox("选择要操作的荣誉ID", achievement_ids)

                try:
                    cursor.execute("SELECT * FROM user_achievements WHERE id = ?", (selected_ach_id,))
                    current_ach = cursor.fetchone()
                    if not current_ach:
                        st.error("❌ 选中的荣誉记录不存在！")
                    else:

                        current_uid, current_award, current_type, current_date, current_org, current_desc = \
                            current_ach[1], current_ach[2], current_ach[3], current_ach[4], current_ach[5], current_ach[6]

                        st.markdown('<h4 style="margin-top:10px;">更新荣誉</h4>', unsafe_allow_html=True)
                        with st.form("update_achievement_form", clear_on_submit=False):
                            default_user_option = f"ID:{current_uid} - {user_dict[str(current_uid)]}"
                            new_user_option = st.selectbox("关联用户*", user_options,
                                                           index=user_options.index(default_user_option))
                            new_award = st.text_input("荣誉名称*", value=current_award)
                            # 新增类别选择（默认选中当前类别）
                            new_type = st.selectbox(
                                "荣誉类别*",
                                ["荣誉", "教育经历", "竞赛", "证书", "账号", "其他"],
                                index=["荣誉", "教育经历", "竞赛", "证书", "账号", "其他"].index(current_type)
                            )
                            new_date = st.date_input("获得日期*",
                                                     value=datetime.strptime(current_date, "%Y-%m-%d").date())
                            new_org = st.text_input("颁发机构", value=current_org)
                            new_desc = st.text_area("荣誉描述", value=current_desc, height=80)

                            submitted_update = st.form_submit_button("确认更新", key="update_btn")
                            if submitted_update:
                                if not new_award.strip():
                                    st.error("❌ 荣誉名称不能为空！")
                                else:
                                    try:
                                        new_uid = new_user_option.split(" - ")[0].replace("ID:", "")
                                        new_uname = user_dict[new_uid]
                                        cursor.execute('''
                                            UPDATE user_achievements
                                            SET user_id = ?, award_name = ?, award_type = ?,
                                                award_date = ?, award_organization = ?, award_description = ?
                                            WHERE id = ?
                                        ''', (new_uid, new_award.strip(), new_type,
                                              new_date.strftime("%Y-%m-%d"), new_org.strip(),
                                              new_desc.strip(), selected_ach_id))
                                        conn.commit()
                                        save_operation("更新荣誉", f"荣誉ID：{selected_ach_id}，用户：{new_uname}，新类别：{new_type}")
                                        st.success(f"✅ 荣誉ID {selected_ach_id} 更新成功！")
                                        st.experimental_rerun()
                                    except sqlite3.Error as e:
                                        st.error(f"更新失败：{str(e)}")

                        st.markdown('<h4 style="margin-top:10px;">删除荣誉</h4>', unsafe_allow_html=True)
                        delete_btn = st.button("确认删除", key="delete_ach_btn")
                        if delete_btn:
                            try:
                                cursor.execute("DELETE FROM user_achievements WHERE id = ?", (selected_ach_id,))
                                conn.commit()
                                save_operation("删除荣誉", f"荣誉ID：{selected_ach_id}，名称：{current_award}，类别：{current_type}")
                                st.success(f"✅ 荣誉ID {selected_ach_id} 已删除！")
                                st.experimental_rerun()
                            except sqlite3.Error as e:
                                st.error(f"删除失败：{str(e)}")
                except sqlite3.Error as e:
                    st.error(f"操作失败：{str(e)}")
            else:
                st.info("ℹ️ 暂无荣誉记录，无法进行更新/删除操作")

        st.markdown('</div>', unsafe_allow_html=True)
    except sqlite3.Error as e:
        st.error(f"用户查询失败：{str(e)}")
        st.markdown('</div>', unsafe_allow_html=True)


elif menu == "3. 个人日程管理":
    st.markdown('<div class="stCard">', unsafe_allow_html=True)

    try:
        cursor.execute("SELECT id, name FROM user_profile ORDER BY id DESC")
        user_list = cursor.fetchall()
        if not user_list:
            st.error("❌ 请先在【个人基本信息管理】中添加用户！")
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            user_dict = {str(user[0]): user[1] for user in user_list}
            user_options = [f"ID:{uid} - {name}" for uid, name in user_list]

            st.markdown('<h3 class="subTitle">➕ 新增个人日程</h3>', unsafe_allow_html=True)
            with st.form("add_schedule_form", clear_on_submit=True):
                col1, col2 = st.columns(2)
                with col1:
                    selected_user_option = st.selectbox("关联用户*", user_options)
                    event_title = st.text_input("日程标题*", placeholder="如：数学考试")
                with col2:
                    st.markdown("**日程时间***")
                    event_date = custom_date_time()
                    event_location = st.text_input("地点", placeholder="如：教学楼301")

                event_description = st.text_area("日程描述", placeholder="请输入日程的详细说明...", height=80)
                submitted_add = st.form_submit_button("确认新增")

                if submitted_add:
                    if not event_title.strip():
                        st.error("❌ 日程标题不能为空！")
                    else:
                        try:
                            selected_uid = selected_user_option.split(" - ")[0].replace("ID:", "")
                            selected_uname = user_dict[selected_uid]
                            cursor.execute('''
                                INSERT INTO user_schedule 
                                (user_id, event_title, event_date, event_location, event_description)
                                VALUES (?, ?, ?, ?, ?)
                            ''', (selected_uid, event_title.strip(), event_date.strftime("%Y-%m-%d %H:%M"),
                                  event_location.strip(), event_description.strip()))
                            conn.commit()
                            save_operation("新增日程", f"用户：{selected_uname}，日程：{event_title.strip()}")
                            st.success("✅ 个人日程新增成功！")
                        except sqlite3.Error as e:
                            st.error(f"新增失败：{str(e)}")

            st.markdown('<h3 class="subTitle">🔍 查看/筛选个人日程</h3>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                filter_uid = st.selectbox("按用户筛选", ["全部"] + user_options)
            with col2:
                filter_date = st.date_input("按日期筛选（可选）", None)

            conditions = []
            params = []

            if filter_uid != "全部":
                filter_uid_val = filter_uid.split(" - ")[0].replace("ID:", "")
                conditions.append("user_id = ?")
                params.append(filter_uid_val)

            if filter_date is not None:
                filter_date_str = filter_date.strftime("%Y-%m-%d")
                conditions.append("DATE(event_date) = ?")
                params.append(filter_date_str)

            base_sql = "SELECT * FROM user_schedule"
            if conditions:
                query_sql = f"{base_sql} WHERE {' AND '.join(conditions)} ORDER BY event_date ASC"
            else:
                query_sql = f"{base_sql} ORDER BY event_date ASC"

            try:
                cursor.execute(query_sql, params)
                schedule_df = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

                if not schedule_df.empty:
                    schedule_df["user_name"] = schedule_df["user_id"].astype(str).map(user_dict)
                    schedule_df = schedule_df[["id", "user_name", "event_title", "event_date",
                                               "event_location", "event_description"]]

                    st.dataframe(
                        schedule_df,
                        use_container_width=True,
                        column_config={
                            "id": st.column_config.NumberColumn("日程ID", width="small"),
                            "user_name": st.column_config.TextColumn("关联用户", width="medium"),
                            "event_title": st.column_config.TextColumn("日程标题", width="medium"),
                            "event_date": st.column_config.DatetimeColumn("日程时间", format="YYYY-MM-DD HH:mm"),
                            "event_location": st.column_config.TextColumn("地点", width="medium"),
                            "event_description": st.column_config.TextColumn("日程描述", width="large")
                        },
                        hide_index=True
                    )

                    binary_data, filename = export_to_csv(schedule_df, "个人日程记录")
                    if binary_data and filename:
                        st.download_button(
                            label="💾 导出CSV文件",
                            data=binary_data,
                            file_name=filename,
                            mime="text/csv"
                        )
                else:
                    st.info("ℹ️ 暂无符合条件的日程记录")
            except sqlite3.Error as e:
                st.error(f"查询失败：{str(e)}")

            st.markdown('<h3 class="subTitle">✏️ 更新/删除个人日程</h3>', unsafe_allow_html=True)
            if not schedule_df.empty:
                schedule_ids = schedule_df["id"].tolist()
                selected_sch_id = st.selectbox("选择要操作的日程ID", schedule_ids)

                try:
                    cursor.execute("SELECT * FROM user_schedule WHERE id = ?", (selected_sch_id,))
                    current_sch = cursor.fetchone()
                    if not current_sch:
                        st.error("❌ 选中的日程记录不存在！")
                    else:
                        current_uid, current_title, current_date, current_loc, current_desc = \
                            current_sch[1], current_sch[2], current_sch[3], current_sch[4], current_sch[5]

                        st.markdown('<h4 style="margin-top:10px;">更新日程</h4>', unsafe_allow_html=True)
                        with st.form("update_schedule_form", clear_on_submit=False):
                            default_user_option = f"ID:{current_uid} - {user_dict[str(current_uid)]}"
                            new_user_option = st.selectbox("关联用户*", user_options,
                                                           index=user_options.index(default_user_option))
                            new_title = st.text_input("日程标题*", value=current_title)

                            st.markdown("**日程时间***")
                            new_date = custom_date_time(
                                default=datetime.strptime(current_date, "%Y-%m-%d %H:%M")
                            )

                            new_loc = st.text_input("地点", value=current_loc)
                            new_desc = st.text_area("日程描述", value=current_desc, height=80)

                            submitted_update = st.form_submit_button("确认更新", key="update_btn")
                            if submitted_update:
                                if not new_title.strip():
                                    st.error("❌ 日程标题不能为空！")
                                else:
                                    try:
                                        new_uid = new_user_option.split(" - ")[0].replace("ID:", "")
                                        new_uname = user_dict[new_uid]
                                        cursor.execute('''
                                            UPDATE user_schedule
                                            SET user_id = ?, event_title = ?, event_date = ?, 
                                                event_location = ?, event_description = ?
                                            WHERE id = ?
                                        ''', (new_uid, new_title.strip(), new_date.strftime("%Y-%m-%d %H:%M"),
                                              new_loc.strip(), new_desc.strip(), selected_sch_id))
                                        conn.commit()
                                        save_operation("更新日程", f"日程ID：{selected_sch_id}，用户：{new_uname}")
                                        st.success(f"✅ 日程ID {selected_sch_id} 更新成功！")
                                        st.experimental_rerun()
                                    except sqlite3.Error as e:
                                        st.error(f"更新失败：{str(e)}")

                        st.markdown('<h4 style="margin-top:10px;">删除日程</h4>', unsafe_allow_html=True)
                        delete_btn = st.button("确认删除", key="delete_sch_btn")
                        if delete_btn:
                            try:
                                cursor.execute("DELETE FROM user_schedule WHERE id = ?", (selected_sch_id,))
                                conn.commit()
                                save_operation("删除日程", f"日程ID：{selected_sch_id}，标题：{current_title}")
                                st.success(f"✅ 日程ID {selected_sch_id} 已删除！")
                                st.experimental_rerun()
                            except sqlite3.Error as e:
                                st.error(f"删除失败：{str(e)}")
                except sqlite3.Error as e:
                    st.error(f"操作失败：{str(e)}")
            else:
                st.info("ℹ️ 暂无日程记录，无法进行更新/删除操作")

        st.markdown('</div>', unsafe_allow_html=True)
    except sqlite3.Error as e:
        st.error(f"用户查询失败：{str(e)}")
        st.markdown('</div>', unsafe_allow_html=True)


elif menu == "4. 操作历史":
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    st.markdown('<h3 class="subTitle">📜 最近操作历史（最多10条）</h3>', unsafe_allow_html=True)

    HISTORY_PATH = Path("operation_history.csv")
    if HISTORY_PATH.exists():
        try:
            history_df = pd.read_csv(HISTORY_PATH, encoding="utf-8-sig")
            if not history_df.empty:
                for _, row in history_df.iterrows():
                    st.markdown(f"""
                        <div class="history-item">
                            <strong>{row['operation']}</strong>
                            <div>{row['details']}</div>
                            <div class="history-time">{row['time']}</div>
                        </div>
                    """, unsafe_allow_html=True)

                clear_btn = st.button("清空操作历史", key="clear_history_btn")
                if clear_btn:
                    try:
                        pd.DataFrame(columns=["time", "operation", "details"]).to_csv(
                            HISTORY_PATH, index=False, encoding="utf-8-sig"
                        )
                        st.success("✅ 操作历史已清空！")
                        st.experimental_rerun()
                    except Exception as e:
                        st.error(f"清空失败：{str(e)}")
            else:
                st.info("ℹ️ 暂无操作记录")
        except Exception as e:
            st.error(f"读取历史失败：{str(e)}")
    else:
        st.info("ℹ️ 暂无操作记录")

    st.markdown('</div>', unsafe_allow_html=True)

conn.close()
