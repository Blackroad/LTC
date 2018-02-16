def test_open_lts(app):
    test_data = app.config
    app.open_home_page()
    app.edit_document()
    app.background.reason_for_change(test_data["RFC"]["type_of_change"],
                                     test_data["RFC"]["reason_for_change"])
    app.background.types_of_Lot_level_change(test_data["types_of_LLC"]["ic_upgrade"],
                                             test_data["types_of_LLC"]["scsp_upgrade"],
                                             test_data["types_of_LLC"]["component"],
                                             test_data["types_of_LLC"]["hybrid_upgrade"],
                                             test_data["types_of_LLC"]["lot_upgrade"])
    app.background.questions(test_data["questions"]["question1"],
                             test_data["questions"]["question2"],
                             test_data["questions"]["question3"],
                             test_data["questions"]["question4"])
    app.background.add_part(test_data["part"]["part_number"],
                            test_data["part"]["part_revision"],
                            test_data["part"]["part_status"])
    if test_data["questions"]["question1"] == 'Yes' and app.error_checker("JDE Part Change")== False:
        app.navigate_to("JDE Part Change")
        app.jde_part_change.fetch_JDE_status(test_data["JDE_Part"]["Propose_LotType"])


