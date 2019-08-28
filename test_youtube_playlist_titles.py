from unittest.mock import MagicMock, patch, call
import youtube_playlist_titles

def test_get_titles_from_page():
    sample_response_json = {
        "items": [
            {
                "snippet": {
                    "title": "Title 1"
                }
            },
            {
                "snippet": {
                    "title": "Title 2"
                }
            },
            {
                "snippet": {
                    "title": "Title 3"
                }
            }
        ]
    }

    titles = youtube_playlist_titles.get_titles_from_page(sample_response_json)
    assert titles == ["Title 1", "Title 2", "Title 3"]


@patch("youtube_playlist_titles.get_page")
def test_get_all_titles_one_page(mock_get_page):
    mock_page = {
        "items": [
            {
                "snippet": {
                    "title": "Title 1"
                }
            },
            {
                "snippet": {
                    "title": "Title 2"
                }
            },
            {
                "snippet": {
                    "title": "Title 3"
                }
            }
        ]
    }
    mock_get_page.return_value = mock_page

    titles = list(youtube_playlist_titles.get_all_titles("test_playlist_id"))

    assert mock_get_page.mock_calls == [call("test_playlist_id")]
    assert titles == ["Title 1", "Title 2", "Title 3"]

@patch("youtube_playlist_titles.get_page")
def test_get_all_titles_two_pages(mock_get_page):
    mock_page_1 = {
        "nextPageToken": "next",
        "items": [
            {
                "snippet": {
                    "title": "Title 1"
                }
            },
            {
                "snippet": {
                    "title": "Title 2"
                }
            },
            {
                "snippet": {
                    "title": "Title 3"
                }
            }
        ]
    }
    mock_page_2 = {
        "items": [
            {
                "snippet": {
                    "title": "Title 4"
                }
            },
            {
                "snippet": {
                    "title": "Title 5"
                }
            },
            {
                "snippet": {
                    "title": "Title 6"
                }
            }
        ]
    }
    mock_get_page.side_effect = [mock_page_1, mock_page_2]

    titles = list(youtube_playlist_titles.get_all_titles("test_playlist_id"))

    assert mock_get_page.mock_calls == [call("test_playlist_id"), call("test_playlist_id", page_token="next")]
    assert titles == ["Title 1", "Title 2", "Title 3", "Title 4", "Title 5", "Title 6"]

