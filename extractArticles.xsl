<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:ndnp="http://www.loc.gov/ndnp"
    xmlns:mets="http://www.loc.gov/METS/"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    xmlns:alto="http://www.loc.gov/standards/alto/ns-v2#"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:output method="text"/>
    
    <xsl:template match="ndnp:issue">
        <xsl:variable name="issue_ref" select="string-join(tokenize(., '/')[position() &lt; last()], '/')"/>
        <xsl:variable name="issue_dir" select="concat('dback_xml_only/', $issue_ref, '/')"/>        
        <xsl:variable name="this_issue" select="doc(concat('dback_xml_only/', .))"/>
        
        <!-- Exclude ill formed or missing files -->
        <xsl:if test="not(. = 'sn90057049/7637/1932060301/1932060301_1.xml') 
                  and not(. = 'sn90057049/7637/1932060701/1932060701_1.xml')
                  and not(. = 'sn90057049/7637/1932121202/1932121202_1.xml')">
            <xsl:variable name="articles" select="doc(concat('dback_xml_only/Article-Level/', substring-before(., '_'), '.xml'))"/>
            
            <!-- Get all text blocks for this issue -->
            <xsl:variable name="issue_blocks">
                <xsl:for-each select="$this_issue//mets:fileSec[1]/mets:fileGrp">
                    <xsl:sequence select="doc(concat($issue_dir, mets:file[@USE='ocr']/mets:FLocat/@xlink:href))//alto:TextBlock"/>
                </xsl:for-each>
            </xsl:variable>
            
            <!-- Get articles for this issue and generate a text file for each one -->
            <xsl:for-each select="$articles//mets:structMap//mets:div[@TYPE='article']">
                <xsl:result-document method="text" href="{concat('extractedArticles/', $issue_ref, '/a', position(), '.txt')}">
                    <xsl:for-each select="descendant-or-self::mets:area">
                        <xsl:for-each select="$issue_blocks//alto:TextBlock[@ID = current()/@BEGIN]">
                            <xsl:for-each select="alto:TextLine">
                                <xsl:value-of select="string-join(alto:String/@CONTENT, ' ')"/>
                                <xsl:text>
</xsl:text>
                            </xsl:for-each>
                            <xsl:text>
    
</xsl:text>
                        </xsl:for-each>
                    </xsl:for-each>
                </xsl:result-document>
            </xsl:for-each>
        </xsl:if>
                
    </xsl:template>    
    
    <xsl:template match="ndnp:reel"/>  
    <xsl:template match="text()"/>
    
</xsl:stylesheet>