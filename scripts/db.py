import os

main = os.path.join("db/main.db")

def insert_table(table_name):
    return f"INSERT INTO {table_name}(guild_id, channel_id) VALUES(?,?)"

def update_table(table_name, channel, guild):
    return f"UPDATE {table_name} SET channel_id = {channel} WHERE guild_id = {guild}"

def select_table(table_name, guild):
    return f"SELECT channel_id FROM {table_name} WHERE guild_id = {guild}"

def delete_table(table_name, guild):
    return f"DELETE FROM {table_name} WHERE guild_id = {guild}"

