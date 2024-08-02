import log
import cli


if __name__ == "__main__":
    try:
        cli.cli_logic()
        import dependency_check
        dependency_check.check_all()
        log.log_message('Check: Checking if github ssh keys are setup correctly...')
        import ssh_check
        ssh_check.check_ssh_key()
    except Exception as error_message:
        log.log_message(str(error_message))
