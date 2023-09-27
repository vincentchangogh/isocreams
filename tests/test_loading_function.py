def test_import():
    import isochrone_fitter

def test_iso_loading():
    test_import()
    filename_to_use="iso_jc_z008s_log_age_7.dat"
    sample_filename=r""
    iso_single=isochrone_fitter.load_isochrones(filename_to_use)
    iso_dict=isochrone_fitter.load_multiple_isochrones("",[filename_to_use])
    assert type(iso_single)==type(pd.DataFrame())
    assert type(iso_dict)==type({})
    assert type(iso_dict[filename_to_use])==type(pd.DataFrame())
    assert iso_dict[filename_to_use]==iso_single