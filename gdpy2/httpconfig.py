"""
Used for low level of different url endpoints for requesting between the official gd server or other gdps servers. 
"""

from typing import Any, Callable, Optional, Type, TypeVar

from attrs import define, field
from yarl import URL

_T = TypeVar("_T")

# Conecept work for fixing http endpoints & dont get me started on gdps paths with  4 slashes -> ////


class url_property:
    """Used as a class method decorator for hooking up and joining urls without the shitty boilerplate code"""
    def __init__(self, wrapped: Callable[..., Any]):
        self.wrapped = wrapped
        self.__doc__ = wrapped.__doc__
        self.name = wrapped.__name__

    def __get__(self, inst: "HTTPConfig", owner: Optional[Type[Any]] = None) -> URL:
        try:
            try:
                return inst.cache[self.name]
            except KeyError:
                val = inst.url / self.wrapped(inst)
                inst.cache[self.name] = val
                return val
        except AttributeError:
            if inst is None:
                return self
            raise

    def __set__(self, inst: "HTTPConfig", value: _T) -> None:
        raise AttributeError("url property is read-only Might change in the future.")


# NOTE: I don't know how we will fix different gdps endpoints in the future. 
# I guess I'll leave that to the other developers to figure out... - Calloc
@define 
class HTTPConfig:
    """Used to help configure ongoing requests back and forth with different servers..."""
    server:str = "https://www.boomlings.com/database"

    url:URL = field(init=False)
    cache:dict[str, URL] = field(init=False, factory=dict)
    def __attrs_post_init__(self):
        self.url = URL(self.server)

    @url_property
    def login(self):
        return "accounts/loginGJAccount.php"
    
    @url_property
    def load(self):
        return "accounts/syncGJAccountNew.php"
    
    @url_property
    def save(self):
        return "accounts/backupGJAccountNew.php"
    
    @url_property
    def get_account_url(self): 
        return "getAccountURL.php"
    
    @url_property
    def get_role_id(self):
        return "requestUserAccess.php"
    
    @url_property
    def update_settings(self):
        return "updateGJAccSettings20.php"
    
    @url_property
    def update_profile(self):
        return "updateGJUserScore22.php"
    
    @url_property
    def get_users(self):
        return "getGJUsers20.php"
    
    @url_property
    def get_user(self):
        return "getGJUserInfo20.php"
    
    @url_property
    def get_relationships(self):
        return "getGJUserList20.php"
    
    @url_property
    def get_leaderboard(self):
        return "getGJScores20.php"
    
    @url_property
    def get_levels(self):
        return "getGJLevels21.php"
    
    @url_property
    def get_timely(self): 
        return "getGJDailyLevel.php"
    
    @url_property
    def get_level(self):
        return "downloadGJLevel22.php"
    
    @url_property
    def report_level(self):
        return "reportGJLevel.php"
    
    @url_property
    def delete_level(self):
        return "deleteGJLevelUser20.php"
    
    @url_property
    def update_level_desc(self):
        return "updateGJDesc20.php"
    
    @url_property
    def upload_level(self):
        return "uploadGJLevel21.php"
    
    @url_property
    def upload_level(self):
        return "rateGJStars211.php"
    
    @url_property
    def rate_demon(self):
        return "rateGJDemon21.php"
    
    @url_property
    def suggest_level(self):
        return "suggestGJStars20.php"

    @url_property
    def get_level_leaderboard(self):
        return "getGJLevelScores211.php"
    
    @url_property
    def unblock_user(self):
        return "unblockGJUser20.php"
    
    @url_property
    def block_user(self):
        return "blockGJUser20.php"
    
    @url_property
    def unfriend_user(self):
        return "removeGJFriend20.php"
    
    @url_property
    def send_message(self):
        return "uploadGJMessage20.php"
    
    @url_property
    def get_message(self): 
        return "downloadGJMessage20.php"
    
    @url_property
    def delete_message(self):
        return "deleteGJMessages20.php"
    
    @url_property
    def get_messages(self):
        return "getGJMessages20.php"
    
    @url_property
    def send_friend_request(self):
        return "uploadFriendRequest20.php"
    
    @url_property
    def delete_friend_request(self):
        return "deleteGJFriendRequests20.php"
    
    @url_property
    def accept_friend_request(self):
        return "acceptGJFriendRequest20.php"
    
    @url_property
    def read_friend_request(self):
        return "readGJFriendRequest20.php"
    
    @url_property
    def  get_friend_requests(self):
        return "getGJFriendRequests20.php"
    
    @url_property
    def like_level(self):
        return "likeGJItem211.php"
    
    @url_property
    def like_user_comment(self):
        return "likeGJItem211.php"
    
    @url_property
    def like_level_comment(self):
        return "likeGJItem211.php"
    
    @url_property
    def post_level_comment(self):
        return "uploadGJComment21.php"
    
    @url_property
    def post_user_comment(self):
        return "uploadGJAccComment20.php"
    
    @url_property
    def delete_level_comment(self):
        return "deleteGJComment20.php"
    @url_property
    def delete_user_comment(self):
        return "deleteGJAccComment20.php"
    
    @url_property
    def get_user_level_comments(self):
        return "getGJCommentHistory.php"
    
    @url_property
    def get_user_comments(self):
        return "getGJAccountComments20.php"
    
    @url_property
    def get_level_comments(self):
        return "getGJComments21.php"

    @url_property
    def get_gauntlets(self):
        return "getGJGauntlets21.php"

    @url_property
    def get_map_packs(self):
        return "getGJMapPacks21.php"
    
    @url_property
    def get_quests(self):
        return "getGJChallenges.php"
    
    @url_property
    def get_chests(self):
        return "getGJRewards.php"
    
    @url_property
    def get_artists(self):
        return "getGJTopArtists.php"
    
    @url_property
    def get_song(self):
        return "getGJSongInfo.php"

BoomlingsConfig = HTTPConfig()
"""Default config for Requesting to Robtop's server"""
