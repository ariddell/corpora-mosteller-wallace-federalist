hunt_v7_filename = 'writings07madiuoft_djvu.txt'

hunt_v7_clean = (
    r'^.*\sTHE WRITINGS OF\s',  # running header
    r'^.*\sJAMES MADISON\S+\s',  # running header
    r'^[Vv][Oo][Ll]\S\s',   # volume
)

# start, stop (inclusive) pairs
hunt_v7_split = {
    'madison-neutral-trade-code201-pp204-211': (
        r'In times of peace among all nations',
        r'of greater length, will be proper.',
    ),
    'madison-neutral-trade-code202-pp214-225': (
        r'[Oo]nly be obliged to repair my loss,',
        r'the doctrine under consideration.',
    ),
    'madison-neutral-trade-code203-pp226-235': (
        r'As the basis of the true doctrine,',
        r'the old, as the only efficacious, expedient.',
    ),
    'madison-neutral-trade-code204-pp235-243': (
        r'The reporter would conclude, from the capture of the neutral',
        r'and to all places not blockaded.',
    ),
    'madison-neutral-trade-code205-pp243-251': (
        r'In a treaty in 1672, between France and Sweden, Arts.',
        r'neutral commerce.',
    ),
    'madison-neutral-trade-code206-pp251-259': (
        r'The treaty of navigation and commerce, March 31, 17 13, be',
        r'towards another nation.',
    ),
    'madison-neutral-trade-code207-pp259-270': (
        r'If there be any parts of the treaty, to which this declaratory',
        r'^enemies.\s+$',
    ),
    'madison-neutral-trade-code208-pp270-278': (
        r'object of dispensing, in time of war, with the navigation',
        r'birth of this spurious principle.',
    ),
    'madison-neutral-trade-code209-pp278-285': (
        r'Being avowed, how\^ever, on the part of the Government, it',
        r'of Prussian ships.',
    ),
    'madison-neutral-trade-code210-pp285-293': (
        r'At the commencement of the war of 1778, the public opinion',
        r'f trade pretermitted.',
    ),
    'madison-neutral-trade-code211-pp293-301': (
        r'^The material article',
        r'''Sir L. Jenkins' wT\)rks, 2 vol., p. 741.''',
    ),
    'madison-neutral-trade-code212-pp302-310': (
        r'^Here the point is clearly established, that a vessel found',
        r'maxims of public morality, as well as of national honor.',
    ),
    'madison-neutral-trade-code213-pp310-319': (
        r'The second pretension subsidiary to the commercial policy',
        r'^\s*the law of nations.\s*$',
    ),
    'madison-neutral-trade-code214-pp319-325': (
        r'These unexampled and vexatious proceedings manifestly',
        r'and to the extent above explained.',
    ),
    'madison-neutral-trade-code215-pp325-334': (
        r'The dilemma was indeed unavoidable',
        r'applicable to the former, as to the latter object.',
    ),
    'madison-neutral-trade-code216-pp334-340': (
        r'But an essential vice of the argument lies in the fallacy of',
        r'^\s*servance of justice.\s*$',
    ),
    'madison-neutral-trade-code217-pp340-349': (
        r'It only remains to advert to a reply, from the judge to the',
        r'^entered the mind of Grotius."',
    ),
    'madison-neutral-trade-code218-pp349-357': (
        r'If by the "carrying trade" Mr. Ward means the carriage of',
        r'plying colonies with contraband."',
    ),
    'madison-neutral-trade-code219-pp357-366': (
        r'Hubner wrote in the war of 1756. Another Danish writer,',
        r'^tion of the principle.',
    ),
    'madison-neutral-trade-code220-pp366-375': (
        r'When Mr. Ward then asks, "where is the man of plain un-',
        r'more, that she ought not.\s+$',
    ),
}
hunt_v7_merge = {}

hunt_v6_filename = 'writings06madiuoft_djvu.txt'
hunt_v6_clean = hunt_v7_clean
hunt_v6_split = {
    'madison-consolidation-code315-pp67-69': (
        r'Much has been said, and not without reason, against a',
        r'of reason, benevolence, and brotherly affection.',
    ),
    'madison-public-opinion-code315-p70': (
        r'Public opinion sets bounds to every government, and is the',
        r'be too extensive.',
    ),
    'madison-money-code302-pp71-80': (
        r'It has been taken for an axiom in all our reasonings on the',
        r'the necessity of emitting hills of credit.',
    ),
    'madison-government-of-the-united-states-code315-pp91-93': (
        r'Power being found by universal experience liable to abuses,',
        r'^other\.\s+$'
    ),
}

hunt_v6_merge = {
    'madison-code315': (
        'madison-consolidation-code315-pp67-69',
        'madison-public-opinion-code315-p70',
        'madison-government-of-the-united-states-code315-pp91-93',
    ),
}
