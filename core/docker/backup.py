import datetime
from fabric import Connection
from core import settings
now = datetime.datetime.now()

file_db = str(now.strftime("%Y-%m-%d-%H-%M") + ".sql")
command_bp = ("pg_dumpall -U dba > " + file_db)
command_docker = ("docker exec -i postgres psql -U dba")

def CreateBackupBot(environment):
    def CreateBackup():
        command = ("docker exec -i postgres " + command_bp)
        if c.run(command).ok:
            print("Dump successfully created")
            print c.host
            return True

    with Connection(
        host=environment,  # PAST there connection hostname variable!
        user="root",
        connect_kwargs={
            "key_filename": "C:\Users\maksym.fillipov\PycharmProjects\\telegram_bot\core\docker\.key"
        },
    ) as c:
        if CreateBackup():
            try:
                backup_name = c.host + "_" + file_db
                c.get(file_db, "C:\\Users\maksym.fillipov\PycharmProjects\postgres\\nectain_bd\\" + backup_name)
                c.run("rm " + file_db)
                print("Successfully copied and removed from server")
                return backup_name
            except:
                print("Something wrong!")

def RestoreBackupBot(source, destination):
    backup_name = CreateBackupBot(source)
    print backup_name
    def RestoreBackup():
        print ("Start restore backup to " + c.host)
        c.put("C:\\Users\maksym.fillipov\PycharmProjects\postgres\\nectain_bd\\"+backup_name, "/")
        print("copy successful")
        c.run("docker cp /"+backup_name + " postgres:/"+backup_name)
        print("Dump copy to container successful")

        c.run(command_docker + " -c " + "SELECT  pg_terminate_backend(pid) FROM pg_stat_activity WHERE pid <> pg_backend_pid();" +"&& " + command_docker + " -c drop database camunda && " + command_docker + " -c create database camunda && " + command_docker + " -c drop database nectain && " + command_docker + " -c create database nectain && " + command_docker + " -f " + " / " +backup_name)
        print ('Restart environment' + c.host)
#        c.run('docker-compose -f /home/gitlab-runner/builds/a42b2c1d/0/nectain/ub-app/docker/nginx+ub+postgres/traefik-compose.yml up --build -d') # PAST there patch to docker-compose file
        c.run('rm /' + backup_name)
        return True

    with Connection(
                host=destination, # PAST there connection hostname variable!
                user="root",
                connect_kwargs={
                    "key_filename": "C:\Users\maksym.fillipov\PycharmProjects\\telegram_bot\core\docker\.key"
                },
    ) as c:
        RestoreBackup()
        print("Database restore " + backup_name + "========> " + c.host )
#RestoreBackupBot(settings.connectToEnvironment["qa"], settings.connectToEnvironment["stage"])