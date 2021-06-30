from simple_term_menu import TerminalMenu
from kubeconfig import KubeConfig

conf = KubeConfig()

dev_menu_with_newline = ["back"]
tst_menu_with_newline = ["back"]
uat_menu_with_newline = ["back"]
prd_menu_with_newline = ["back"]
# set k8_context_list with output from kube config file
with open('/users/kgambill/.kube/config') as kube_config:
    for line in kube_config:
        if '- name' in line:
           ctx = line.split(":", 1)
           if 'dev' in line:
               dev_menu_with_newline.append(ctx[1])
           if 'tst' in line:
               tst_menu_with_newline.append(ctx[1])
           if 'uat' in line:
               uat_menu_with_newline.append(ctx[1])
           if 'prd' in line:
               prd_menu_with_newline.append(ctx[1])
dev_spaces = [s.replace("\n", "") for s in dev_menu_with_newline]
tst_spaces = [s.replace("\n", "") for s in tst_menu_with_newline]
uat_spaces = [s.replace("\n", "") for s in uat_menu_with_newline]
prd_spaces = [s.replace("\n", "") for s in prd_menu_with_newline]
dev_menu_items = [s.replace(" ", "") for s in dev_spaces]
tst_menu_items = [s.replace(" ", "") for s in tst_spaces]
uat_menu_items = [s.replace(" ", "") for s in uat_spaces]
prd_menu_items = [s.replace(" ", "") for s in prd_spaces]

def main():
    main_menu_title = "   Set Kubectl Context\n"
    main_menu_items = ["dev", "tst", "uat", "prd", "quit"]
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_red", "bold")
    main_menu_style = ("bold", "fg_gray")
    main_menu_exit = False

    main_menu = TerminalMenu(
        title=main_menu_title,
        menu_entries=main_menu_items,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    dev_menu_title = " DEV Menu\n"
    #dev_menu_items = ["back\n", "dev 2\n", "dev 3\n"]
    dev_menu_back = False
    dev_menu_style = ("standout", "fg_green")
    dev_menu = TerminalMenu(
        dev_menu_items,
        title=dev_menu_title,
        menu_cursor=main_menu_cursor,
        menu_highlight_style=dev_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    tst_menu_title = " TST Menu\n"
    tst_menu_back = False
    tst_menu_style = ("standout", "fg_yellow")
    tst_menu = TerminalMenu(
        tst_menu_items,
        title=tst_menu_title,
        menu_cursor=main_menu_cursor,
        menu_highlight_style=tst_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    uat_menu_title = " UAT Menu\n"
    uat_menu_back = False
    uat_menu_style = ("standout", "fg_purple")
    uat_menu = TerminalMenu(
        uat_menu_items,
        title=uat_menu_title,
        menu_cursor=main_menu_cursor,
        menu_highlight_style=uat_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    prd_menu_title = " PRD Menu\n"
    prd_menu_back = False
    prd_menu_style = ("standout", "fg_red")
    prd_menu_exit = False
    prd_menu = TerminalMenu(
        prd_menu_items,
        title=prd_menu_title,
        menu_cursor=main_menu_cursor,
        menu_highlight_style=prd_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )
    while not main_menu_exit:
        main_select = main_menu.show()
        if main_select == 0:
            dev_menu_back = False
            while not dev_menu_back:
                dev_select = dev_menu.show()
                if dev_select != 0 & dev_select != "None":
                    conf.use_context(dev_menu_items[dev_select])
                    dev_menu_back = True
                    main_menu_exit = True
                    print(f"set context to: {dev_menu_items[dev_select]}")
                if dev_select == 0:
                    dev_menu_back = True

        if main_select == 1:
            tst_menu_back = False
            while not tst_menu_back:
                tst_select = tst_menu.show()
                if tst_select != 0 & tst_select != "None":
                    conf.use_context(tst_menu_items[tst_select])
                    tst_menu_back = True
                    main_menu_exit = True
                    print(f"set context to: {tst_menu_items[tst_select]}")
                if tst_select == 0:
                    tst_menu_back = True

        if main_select == 2:
            uat_menu_back = False
            while not uat_menu_back:
                uat_select = uat_menu.show()
                if uat_select != 0 & uat_select != "None":
                    conf.use_context(uat_menu_items[uat_select])
                    uat_menu_back = True
                    main_menu_exit = True
                    print(f"set context to: {uat_menu_items[uat_select]}")
                if uat_select == 0:
                    uat_menu_back = True

        if main_select == 3:
            prd_menu_back = False
            while not prd_menu_back:
                prd_select = prd_menu.show()
                if prd_select != 0 & prd_select != "None":
                    conf.use_context(prd_menu_items[prd_select])
                    prd_menu_back = True
                    main_menu_exit = True
                    print(f"set context to: {prd_menu_items[prd_select]}")
                if prd_select == 0:
                    prd_menu_back = True
        if main_select == 4:
            main_menu_exit = True
            print("Quitting!")


if __name__ == "__main__":
    main()
