def calculate_metrics(staff_rawdata):
    # Calculate DDM
    staff_rawdata['ddm'] = ((staff_rawdata['Det'] + staff_rawdata['Dis'] + staff_rawdata['Mot']) / 3).round(1)

    # Calculate Scout
    staff_rawdata['scout'] = ((staff_rawdata['Ada'] + staff_rawdata['Judge A'] + staff_rawdata['Judge P']) / 3).round(1)

    # Calculate Scout Overall
    staff_rawdata['scoutOv'] = ((staff_rawdata['scout'] + staff_rawdata['ddm']) / 2).round(1)

    return staff_rawdata[['Inf', 'Name', 'Preferred Job', 'Club', 'ddm', 'scout', 'scoutOv']] 