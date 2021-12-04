## Notes

1. The app works as requested.

2. The test case 'list when there are no remaining tasks' in `task.test.js` file did not clear the tasks list before checking. This lead to test case failure. so to correct it the following line of code was added to it.
    ```
    [3, 2, 1].forEach((n) => execSync(tasksTxtCli("del", n.toString())))
    ```
3. An extra list reset feature was added which clears all the items in the pending list and also the completed list.
   ```
   .\task.sh reset
   ```
4. To do multiple tests, clear the list using the above reset command to avoid testcase errors.
5. If the `task.db` file is not presen. use the same reset command to initialize it.
6. Use the following command for more help.
    ```
    .\task.sh help
    ```
