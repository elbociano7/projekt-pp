class Database:
  def get(self, field: str, value: any, object: object):
    sql = "SELECT 1 FROM "+object.getTableName()+"WHERE "+field+"=`"+value+"`"
    
