DEFAULT_SETTINGS = {
    "update_interval": 0.01,
    "hardware": {
        "device_id": 0  # only change if use more than one corsair device, and it's interfering with the program
    },
    "renders": {
        "active": ["BackgroundRender", "HpRender", "WeaponRender", "BombRender", "FlashbangRender"],
        "settings": {
            "BackgroundRender": {
                "ct_color": "#5C7793",
                "t_color": "#C16734"
            },
            "BombRender": {
                "explode_time": 40
            },
            "FlashbangRender": {
                "gradient": True
            }
        }
    }
}
