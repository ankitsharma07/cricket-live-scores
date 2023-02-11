#!/usr/bin/env python3

import feedparser


class LiveFeedParser:
    def __init__(self, rss_url):
        self.url = rss_url

    def get_all_scores(self):
        response = feedparser.parse(self.url)
        match_feeds = response.get("entries", [])
        return self._get_scores(match_feeds)

    @staticmethod
    def _get_scores(match_feeds):
        live_scores = []
        return live_scores
